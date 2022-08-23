import random
Sentence_starter =[item for item in input("Enter the list items : ").split()] #['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character =[item for item in input("Enter the list items : ").split()] #[' there lived a king.',' there was a man named Jack.',
			' there lived a farmer.']
time =[item for item in input("Enter the list items : ").split()] #[' One day', ' One full-moon night']
story_plot =[item for item in input("Enter the list items : ").split()] #[' he was passing by',' he was going for a picnic to ']
place =[item for item in input("Enter the list items : ").split()] #[' the mountains', ' the garden']
second_character =[item for item in input("Enter the list items : ").split()] #[' he saw a man', ' he saw a young lady']
age =[item for item in input("Enter the list items : ").split()] #[' who seemed to be in late 20s', ' who seemed very old and feeble']
work =[item for item in input("Enter the list items : ").split()] #[' searching something.', ' digging a well on roadside.']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work)+random.choice(lst2))
