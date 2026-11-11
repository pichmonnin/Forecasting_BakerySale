def set_qaurtile(count):
    "count : Take the count value"
    q1, q2, q3 = count.quantile([0.25, 0.5, 0.75])
    return {
        "bottom-Tier": count[count < q1],
        "Lower-Mid-Tier": count[(count >= q1) & (count <= q2)],
        "Upper-Mid-Tier": count[(count >= q2) & (count < q3)],
        "Upper-Tier": count[count >= q3],
    }
