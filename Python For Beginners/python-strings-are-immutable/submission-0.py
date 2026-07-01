def remove_fourth_character(word: str) -> str:
    before_w = word[:3]
    after_w = word[4:]

    new_balance = before_w + after_w
    return new_balance


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
