#!/bin/sh
#
# NAME
# git-draw - draws nearly the full content of a tiny git repository as a graph
#
# SYNOPSIS
# git-draw [OPTION]...
#
# PREREQUISITES
# You don't need graphviz or imagemagick if you use git-draw with certain
# options.
#
# - perl
# - graphviz (http://www.graphviz.org/)
# - imagemagick (http://www.imagemagick.org)
#
# If you have apt you can install these with:
#
# sudo apt-get install perl graphviz imagemagick
#
# DESCRIPTION
# git-draw is composed of three main steps, where the 2nd and 3rd are just
# for convenience and are not part of git-draw's core responsibility.
#
# 1) A .dot file describing the repository's content as a graph is created.
# 2) dot (see graphviz) is called to produce an image out of that .dot file.
# 3) display (see imagemagick) is called to display that image.
#
# Because git-draw currently is quite dumb, the current working directory
# must be at the root of the working tree of your project, i.e. the
# directory which contains the .git directory.
#
# The intention is to help learning Git's basic concepts (references, Git
# objects, SHA-1 checksum over content as id). Virtually all information
# concerning Git's basic concepts is contained in the drawing. Thus git-draw
# is aimed at tiny toy Git repositories and at users with an engineer
# background, i.e. users which are not scared off by terms like checksum,
# references aka pointers and graphs.
#
# OPTIONS
# -p, --print-only
# Only prints the .dot file to STDOUT. Mutually exclusive with
# --image-only.
#
# -i, --image-only
# Only generates an image of the graph, and a .dot file beforehand.
# Mutually exclusive with --print-only.
#
# AUTHOR
# Written by Florian Kaufmann <sensorflo@gmail.com>
#
# COPYRIGHT
# Florian Kaufmann 2014. License GPLv3+: GNU GPL version 3 or later
# <http://gnu.org/licenses/gpl.html>. This is free software: you are free to
# change and redistribute it. There is NO WARRANTY, to the extent permitted
# by law.
#
# SEE ALSO
# git(1)

# $1 = exit code
print_usage_and_exit() {
  cat <<EOF
Usage: git-draw [--help] [-p|--print-only] [-i|--image-only]"
-p|--print-only Only print .dot to stdout."
-i|--image-only Only create an image, and a .dot file beforehand."

The primary documentation is at the top of the git-draw script itself, see
$(type -p git-draw)
EOF
  exit $1
}

# TODO
# - Layout graph so commit DAG is top-down and on the left, probably using
# graphviz's ranks.
# - Auto-number output files so user can see / compare the different states
# of the repository was in.
# - Optionally use temporary files which the user does not directly see
# - Optionally omit drawing the content of all/certain objects/refs so a
# bit
# larger than tiny repositories still draw usefully.
# - tree objects / reflogs shall fan out graph edges at corresponding line
# in
# content
# - Amend type cell (top left) and id cell (top right) with the prefix
# 'type=' and 'id=' to be very clear. Optionally turn off with options.
# - add a graph title / caption which tells the git command(s) since the
# last
# version of the repository content.
# - Provide options to choose the tool to display the image outputted by
# dot.
# - Support for all those possible other layouts of git repositories. Bare
# repository, a .git file at the root pointing to the real directory,
# environment variables etc. Most probably by using git commands
# exclusive opposed to directly access files within .git, or by asking
# git for the path to the repository.
# - Read gitrepository-layou(1) to find out more things which could be
# displayed
# - To be on the safe side, quote _all_ non-alphanumeric characters in
# label strings of a dot 'program'.
# - Draw multiple repos in one image. Usefull to demonstrate distributed git.
# - Add a fourth element (beside type/id/content) to the things: also the
# config properties. E.g for a branch it's remote tracking branch.
# - Draw packed objects and refs in a subgraph respectively.
# - Allow that the current working directory can be any subdirectory of a
# git project. Similarly, allow to specify the git repository via command
# line arguments.

abbreviate_sha1() {
  # BUG: in a blob or commit-msg, would also replace what looks like a sha1
  perl -pe 's/([0-9a-f]{40})/substr(`git rev-parse --short=4 $1`,0,-1)/eg'
}

ls_all_objects() {
  # unpacked objects
  find .git/objects/ -type f |
    perl -ne 'print "$1$2\n" if m@^.*/([a-f0-9]{2})/([a-f0-9]{38})@'

  # packed objects
  # note that the .idx is not always present
  find .git/objects/pack/ -iname '*.idx' | while read idxfile; do
cat $idxfile | git show-index |
      perl -pe 's@^.*?([a-f0-9]{40}).*$@$1@'
  done
}

ls_all_refs() {
  # todo: refs like MERGE_HEAD are still not printed
  git show-ref --abbrev=4
  cat .git/HEAD | perl -ne '
m/^(?:ref: )?(.*?)$/;
if ($1 =~ m/([a-f0-9]{40})/) {
$idshort = substr(`git rev-parse --short=4 $1`,0,-1);
}
else { $idshort = $1 }
print $idshort . " HEAD\n";'
}

ls_all_objects_short() {
  ls_all_objects | while read sha1; do
git rev-parse --short=4 $sha1
  done
}

print_dot_objects() {
  ls_all_objects_short | while read id; do
dotid="_$id"
    object_type=$(git cat-file -t $id)
    objcontent=$(git cat-file -p $id | abbreviate_sha1 |
      perl -pe 's/([^a-zA-Z0-9\n\r])/\\$1/g; s/(\r?\n)?$/\\l/;')
    case $object_type in
      commit) fillcolor=palegreen1;;
      tag) fillcolor=lightyellow;;
      *) fillcolor=white;;
    esac
echo " $dotid [fillcolor=$fillcolor, style=\"filled,rounded\", "\
      "label=\"{{obj:$object_type|$id}|$objcontent}\"]"

    # todo: use git's commands to extract the object references
    # BUG: must escape stuff that .dot interprets (\n,\l,\l,|,{},...)
    # BUG(obsolete when using git's cmds): cannot deal with multiple sha1 on one line
    # BUG(obsolete when using git's cmds): in a blob or commit-msg, would also
    # replace what looks like a sha1
    git cat-file -p $id |
      perl -ne 'print " '$dotid' -> _" .
`git rev-parse --short=4 $1` if /([a-f0-9]{40})/'
  done

git fsck --cache --unreachable --dangling 2>/dev/null |
   perl -ne 'print " _" . substr(`git rev-parse --short=4 $1`,0,-1) .
" [style=dotted]\n" if /^(?:dangling|unreachable)\b.*?([a-f0-9]{40})/'
}

print_dot_references() {
  ls_all_refs |
    perl -ne '
if (m@(\S+)\s+(\S+?)$@) {
$me = $2;
$other = $1;
$dotid_me = "_" . (($tmp = $me) =~ s@([^a-zA-Z0-9_])@___@g,$tmp);
$dotid_other = "_" . (($tmp = $other) =~ s@([^a-zA-Z0-9_])@___@g,$tmp);
($otherquoted = $other) =~ s/([^a-zA-Z0-9\n])/\\$1/g;
($mequoted = $me) =~ s/([^a-zA-Z0-9\n])/\\$1/g;
$reftype = "";
$fillcolor = "gray";
$configmetadata = "";
if ($me =~ m@^refs/heads/@) {
$reftype = ":local branch";
($me_short = $me) =~ s@^refs/heads/@@;
$remote = substr(`git config --get branch\\.$me_short\\.remote`,0,-1);
$merge = substr(`git config --get branch\\.$me_short\\.merge`,0,-1);
if ($remote && $merge) {
if ($remote eq ".") {
$dotid_merge = "_" . (($tmp = $merge) =~ s@([^a-zA-Z0-9_])@___@g,$tmp);
} else {
$dotid_merge_core = $merge;
$dotid_merge_core =~ s@^refs/heads/@@;
$dotid_merge_core =~ s@([^a-zA-Z0-9_])@___@g;
$dotid_remote = (($tmp = $remote) =~ s@([^a-zA-Z0-9_])@___@g,$tmp);
$dotid_merge = "_refs___remotes___${dotid_remote}___${dotid_merge_core}";
}
print " $dotid_me -> $dotid_merge [style=dotted, color=gray, fontcolor=gray, " .
"label=\"upstream branch\"]\n";
$tmp = "remote = $remote\nmerge = $merge\n";
$tmp =~ s/([^a-zA-Z0-9\n])/\\$1/g; # quote for dot
$tmp =~ s/\n/\\l/g; # \l instead \n newline
$configmetadata = "|$tmp"
}
}
elsif ($me =~ m@^refs/remotes/@) {
$reftype = ":remote tracking branch";
$fillcolor = "yellow";
}
elsif ($me =~ m@^refs/tags/@) {
$reftype = ":tag";
$fillcolor = "lightyellow";
}
if ( ($other !~ m/^[a-f0-9]+$/) &&
0!=system("git show-ref --verify --quiet -- $other") ) {
print " $dotid_me [style=filled, fillcolor=red, " .
"label=\"{{ref$reftype|$mequoted}|" .
"$otherquoted (referee does not exist)\\l$configmetadata}\"]\n";
} else {
if ($me eq "HEAD") {
$fillcolor="gray30";
$fontcolorelement = "fontcolor=white, ";
}
print " $dotid_me [style=filled, fillcolor=$fillcolor, $fontcolorelement " .
"label=\"{{ref$reftype|$mequoted}|$otherquoted\\l$configmetadata}\"]\n";
print " $dotid_me -> $dotid_other\n";
}
}'
}

print_dot_ref_logs() {
  firstiter="non-empty-string" # i.e. true
  git show-ref --abbrev=4 |
    # The following code depends upon HEAD being the last in the list
    perl -pe 's@^.*?(\brefs/\S*)$@$1@; END { print "HEAD\n";}' |
    while read refname; do
      # work around the problem that 'git reflog show HEAD' results in an
      # error when HEAD contains refs/heads/master but refs/heads/master does
      # not exist, which is the case after 'git init'.
      if [ ! \( "$firstiter" -a \( "$refname" = HEAD \) \) ]; then
        # 8eb068f master@{11}: commit: tempo-ext: new version
        git reflog show $refname | perl -ne '
BEGIN {
$refname = "'$refname'";
$dotid_reflog = "reflog_" . (($tmp = $refname) =~ s@([^a-zA-Z0-9_])@___@g,$tmp);
}
if (m/^([a-f0-9]+).*@\{\d+\}: (.*?)$/) { $id_any=$1; $msg=$2; }
elsif (m/^([a-f0-9]+)/) { $id_any=$1; $msg="<lastentry>"; }
$id_short = substr(`git rev-parse --short=4 $id_any`,0,-1);
print " $dotid_reflog -> _$id_short [color=gray90]\n";
s/^[a-f0-9]+//; # strip sha1; $id_short will be used instead
s/([^a-zA-Z0-9\n])/\\$1/g; # quote for dot
s/(\r?\n)?$/\\l/; # \l instead \n newline, and ensure \l at
# end of content
$content = $content . $id_short . $_;
END {
$trailing = (substr($content,-2) eq "\\l") ? "" : "\\l";
print " $dotid_reflog [color=gray90, fontcolor=gray, " .
"label=\"{{reflog|logs/$refname}|$content$trailing}\"]\n";
}'
      fi
firstiter="" # empty stringt, i.e. false
  done
}

print_dot_index() {
  git ls-files --stage --abbrev=4 | perl -ne '
if (/^[0-9]+\s+([a-f0-9]+)/) {
print " index -> _$1\n";

s/([^a-zA-Z0-9\r\n])/\\$1/g; # quote for dot
s/(\r?\n)?$/\\l/; # \l instead \n newline, and ensure \l at
# end of content
$content = $content . $_;
}
END {
$trailing = (substr($content,-2) eq "\\l") ? "" : "\\l";
print " index [style=filled, fillcolor=lightcyan, " .
"label=\"{{index}|$content$trailing}\"]\n";
}'
}

print_dot() {
  echo "digraph structs {"
  echo " node [shape=record,fontsize=11];"
  echo " subgraph cluster_0 {"
  echo " color=gray80;"
  echo " label = \"legend\\l\";"
  echo " legend_node [label=\"{{type:subtype|id/name}|content\\l|metadata from config\\l}\"]"
  echo " }"

  print_dot_objects
  print_dot_references
  print_dot_ref_logs
  print_dot_index
  echo "}"
}

# process options
dotfilename=git-draw.dot
imgfilename=git-draw.png
if [ $# = 0 ]; then
  :
elif [ \( $# = 1 \) -a \( "$1" = "-p" -o "$1" = "--print-only" \) ] ; then
print_only=1
elif [ \( $# = 1 \) -a \( "$1" = "-i" -o "$1" = "--image-only" \) ] ; then
image_only=1
elif [ \( $# = 1 \) -a \( "$1" = "--help" \) ] ; then
print_usage_and_exit 0
else
echo "Invalid options" >&2
  print_usage_and_exit 1 >&2
  exit 1
fi

# check preconditions
if [ ! -d .git ]; then
echo "Not a git repository" >&2
  exit 1
fi
if ! which perl >&2 >/dev/null; then
cat >&2 <<EOF
perl not found. If you have apt-get, you can install it with 'sudo apt-get
install perl'.
EOF
  exit 1
fi

# generate .dot file
if [ "$print_only" = 1 ] ; then
print_dot
  exit 0
fi
print_dot >"$dotfilename" || exit 1

# build and image out of the .dot file
if ! which dot >&2 >/dev/null; then
cat >&2 <<EOF
dot (part of graphviz) not found. Either use the --print-only option, or
install graphviz. If you have apt-get, you can do that with 'sudo apt-get
install graphviz'.
EOF
  exit 1
fi
dot -Tpng "$dotfilename" > "$imgfilename" || exit 1

# display image
if [ "$image_only" = 1 ] ; then
exit 0
fi
if ! which display >&2 >/dev/null; then
cat >&2 <<EOF
display (part of imagemagick) not found. Image '$imgfilename' was generated,
but I cannot display it. Either use the --image-only option, or install
imagemagick. If you have apt-get, you can do that with 'sudo apt-get install
imagemagick'.
EOF
  exit 1
fi
display "$imgfilename"

