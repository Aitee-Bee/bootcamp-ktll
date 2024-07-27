def groups_per_users(grouppe):
    new_group = {}
    for group, users in grouppe.items():
        for user in users:
            new_group[user] = []
            if user in group:
                new_group[user].append(group)  
            new_group[user].append(group)
    return new_group


print(
    groups_per_users(
        {
            "local": ["admin", "userA"],
            "public": ["admin", "userB"],
            "administrator": ["admin"],
        }
    )
)
