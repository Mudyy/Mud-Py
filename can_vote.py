def can_vote(age):
  if age >= 18:
    return "You can vote"
  else:
    return "Too young to vote"

print(can_vote(20))
print(can_vote(15))
