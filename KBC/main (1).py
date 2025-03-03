questions = [
  [ 
    "The language of Lakshadweep. a Union Territory of India, is","Tamil","Hindi","Malayalam","Telugu", 3
  ],
[
"Bahubali festival is related to",'Islam','Hinduism','Buddhism','Jainism]', 4
],
  [ 
'September 27 is celebrated every year as','Teachers Day','National Integration Day','World Tourism Day','International Literacy Day', 3
],
  ['The death anniversary of which of the following leaders is observed as Martyrs Day?','Smt. Indira Gandhi','PI. Jawaharlal Nehru','Mahatma Gandhi','Lal Bahadur Shastri', 3
],
  [
   "Who is the author of the epic 'Meghdoot'?",'Vishakadatta','Valmiki','Banabhatta','Kalidas',4
  ],
[
  'World Health Day is observed on','Apr 7','Mar 6','Mar I5','Apr 28',1
],
  [
    'Which of the following is observed as Sports Day every year?','22nd April','26th  july','29th August','2nd October',3
  ],
  [
   'Pongal is a popular festival of which state?','Karnataka','Kerala','Tamil Nadu','Andhra Pradesh',3
  ],
  [
   'Ghototkach in Mahabharat was the son of','Duryodhana','Arjuna','Yudhishthir','Bhima',4
  ],
  [
   'Van Mahotsav was started by','Maharshi Karve','Bal Gangadhar Tiiak','K.M, Munshi','Sanjay Gandhi',3
  ],
  [
   'The first month of the Indian national calendar is','Magha','Chaitra','Ashadha','Vaishakha',2
  ],
[
  'Which of the following is not a dance from Kerala?','Kathakali','Mohiniattam','Ottan Thullal','Yaksha Gana',4
],
[
  'Rath Yatra is famous festival at','Ayodhya','Mathura','Dwaraka','Puri',4
],
  [
   'Which of the following is/are youth organisations?','1. NCC 2. NSS 3. NYK','1 only',' 2 only','1 and 2','1,2 and3',4
  ],
  [
    " The abbreviation  'fob' stands for ",'Free on Board.','Free of Bargain','Fellow of Britain','None  of these',1
  ],
]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
3
for i in range(0,len(questions)):
  question = questions[i]
  print(f"\n\nQuestions for Rs. {levels[i]}")
  print(question[0])
  print(f"1.{question[1]}           2.{question[2]} ")
  print(f"3.{question[3]}           4.{question[4]} ")
  reply = int(input('Enter your answer or 0 to  quit : '))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"\ncorrect answer, you have won Rs.   {levels[i]}")
    if (i== 0 ):
      money = 0
    elif (i == 4):
      money = 10000 
    elif(i == 9):
      money = 3200000
    elif(i == 14):
      money = 10000000
  else:
    print("wrong answer")
    break

print(f"\n\n\nYOU HAVE WON AMOUNT : Rs {money}")
    