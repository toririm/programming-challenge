n = input()
m = input()
log_m = len(m) - 1
ans = "0" * (log_m - len(n)) + n
ans = ans[:-log_m] + "." + ans[-log_m:]
ans = ans.rstrip("0")
if ans[-1] == ".":
    ans = ans[:-1]
if ans[0] == ".":
    ans = "0" + ans
print(ans)
