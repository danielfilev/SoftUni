def grocery_store(**kwargs):
    sorted_kwargs = [f"{key}: {value}"for key, value in sorted(
        kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return "\n".join(sorted_kwargs)
