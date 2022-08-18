def computepay(p_hrs, p_rate):
    h = float(p_hrs)
    r = float(p_rate)
    if h > 40:
        base_pay = 40 * r
        overtime_pay = abs(h - 40) * (r * 1.5)
        net_pay = base_pay + overtime_pay
    else:
        net_pay = h * r

    return net_pay


hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(hrs, rate)
print("Pay", p)
