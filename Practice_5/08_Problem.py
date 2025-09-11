user_preferences = {
  "timezone": "GMT",
  "language": "English",
  "notifications": "USD", 
  "theme": None
}

def update_peferences(user_pref):
  return {key: value for key, value in user_pref.items() if value is not None}
#   updated_prefernces = {}

# for key, value in user_pref.items():
#   if value is not None:
#     update_preferences[key] = value
#     return update_preferences

print(update_preferences(user_preferences))
