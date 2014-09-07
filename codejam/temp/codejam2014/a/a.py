# coder : Himanshu Mishra
# Problem A. Magic Trick


def main():
    # no of test cases
    n = int(input())
    for i in range(n):
        ans1 = int(input())
        p = [[int(j) for j in (input().split(" "))],
        [int(j) for j in (input().split(" "))],
        [int(j) for j in (input().split(" "))],
        [int(j) for j in (input().split(" "))]]

        ans2 = int(input())
        q = [[int(j) for j in (input().split(" "))],
        [int(j) for j in (input().split(" "))],
        [int(j) for j in (input().split(" "))],
        [int(j) for j in (input().split(" "))]]

        rowP = p[ans1-1]
        rowQ = q[ans2-1]
        x = (set(rowP)).intersection(set(rowQ))
        if len(x) == 1:
            print("Case #%d:"%(i+1),x.pop())
        elif len(x) > 1:
            print("Case #%d:"%(i+1),"Bad magician!")
        elif len(x) == 0:
            print("Case #%d:"%(i+1),"Volunteer cheated!")


if __name__ == '__main__':
    main()
