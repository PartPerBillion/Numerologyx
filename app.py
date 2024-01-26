import streamlit as st 
import string

numerology_dict = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1, 'J': 1,
    'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4,
    'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
}

number_character = {
    1 : """Number 1: The Leader

Traits and Characteristics

Individuals with a number 1 vibration are known for their confidence, independence, and ambition. They possess strong willpower and determination, which drives them to achieve their goals. As natural-born leaders, they uniquely inspire and motivate others, making them great visionaries and pioneers in their chosen fields.

Challenges and Lessons

Despite their many strengths, number 1 individuals may face challenges related to arrogance, impatience, and a tendency to dominate others. To overcome these obstacles, they
must learn to collaborate effectively, listen to other’s perspectives, and cultivate humility in their interactions.""",
2: """Number 2: The Diplomat

Traits and Characteristics

People with a number 2 vibration are characterized by their diplomatic nature, a strong sense of harmony, and an innate ability to cooperate with others. Their highly developed intuition enables them to foster supportive relationships and mediate conflicts. Their gentle and empathetic nature makes them excellent partners and friends.

Challenges and Lessons

Number 2 individuals often struggle with indecisiveness and can be overly sensitive. To overcome these challenges, they must learn to trust their instincts, stand up for themselves, and find the right balance between assertiveness and diplomacy.""",
3: """Number 3: The Communicator

Traits and Characteristics

Number 3 individuals are known for their creative, expressive, and social nature. They have a natural talent for communication, whether through writing, speaking, or artistic endeavors. Their optimistic and enthusiastic outlook on life can inspire others to follow their lead and pursue their dreams.

Challenges and Lessons

Their main challenges involve self-doubt, scattered energy, and a tendency to procrastinate. To reach their full potential, number 3 individuals must learn to focus on their goals, develop self-discipline, and trust their abilities.""",
4:"""Number 4: The Builder

Traits and Characteristics

Individuals with a number 4 vibration are practical, hardworking, and reliable. They excel at creating solid foundations and value stability in their lives. Their strong organizational skills and attention to detail make them effective problem solvers and successful in their chosen professions.

Challenges and Lessons

Number 4 individuals may struggle with rigidity, stubbornness, and resistance to change. To overcome these challenges, they must embrace flexibility, adapt to new situations, and be open to different perspectives.""",
5:"""Number 5: The Adventurer

Traits and Characteristics

People with a number 5 vibration are characterized by their adventurous spirit, adaptability, and a strong desire for freedom. They are constantly seeking new experiences and thrive in dynamic environments. Their versatility and quick-thinking abilities make them natural problem solvers and agents of change.

Challenges and Lessons

Number 5 individuals often face challenges related to impulsiveness, restlessness, and a lack of direction. They must learn to cultivate discipline, set long-term goals, and develop a sense of commitment to overcome these obstacles.""",
6:"""Number 6: The Nurturer

Traits and Characteristics

Individuals with a number 6 vibration are compassionate, caring, and responsible. They have a strong sense of duty and are dedicated to helping others. Their nurturing nature makes them excellent caregivers, friends, and family members.

Challenges and Lessons

Number 6 individuals may struggle with codependency, a tendency to worry excessively, and difficulty setting boundaries. To overcome these challenges, they must learn to practice self-care, establish healthy boundaries, and balance supporting others and maintaining their well-being.""",
7:"""Number 7: The Seeker

Traits and Characteristics

People with a number 7 vibration are reflective, analytical, and spiritual. They have a natural inclination toward seeking knowledge and wisdom and are often drawn to the deeper mysteries of life. Their intuitive and intellectual abilities make them excellent researchers, philosophers, and spiritual guides.

Challenges and Lessons

Number 7 individuals often face isolation, perfectionism, and skepticism challenges. To overcome these obstacles, they must learn to trust their intuition, embrace life’s imperfections, and develop meaningful connections with others while maintaining their need for solitude and contemplation.""",
8:"""Number 8: The Executive

Traits and Characteristics

Individuals with a number 8 vibration are ambitious, powerful, and goal-oriented. They possess strong leadership qualities and a keen sense of business and finance. Their drive for success often leads them to excel in their chosen fields, making them effective executives and entrepreneurs.

Challenges and Lessons

Number 8 individuals may struggle with a tendency toward materialism, workaholism, and power struggles. To overcome these challenges, they must learn to balance their professional ambitions with their personal lives, practice humility, and develop a sense of empathy and compassion for others.""",
9:"""Number 9: The Humanitarian

Traits and Characteristics

People with a number 9 vibration are compassionate, romantic, and selfless. They have a strong sense of social responsibility and are dedicated to improving the world. Their innate wisdom and spiritual awareness make them excellent teachers, healers, and advocates for social justice.

Challenges and Lessons

Number 9 individuals often face challenges related to self-sacrifice, martyrdom, and a tendency to neglect their needs. To overcome these obstacles, they must learn to set boundaries, prioritize self-care, and recognize that they can serve others better by maintaining their well-being."""
}

def numerology(x):
    # x = 'SRIHARI IS THE GREATEST of all time of all space'
    print(x)
    x = x.replace(' ','')
    x = x.upper()
    for i in x: 
        if i in string.punctuation: 
            x = x.replace(i,'')
    sumx = 0
    for i in x:
        # print(i,'-',numerology_dict[i])
        st.caption(f'{i}/t - {numerology_dict[i]}')
        sumx += numerology_dict[i]
    st.caption(f'Sum - {sumx}')
    print('Sum - ',sumx)
    number = sumx
    while len(str(number))>1:
        sumx = 0
        for i in str(number):
            sumx+=int(i)
            st.caption(f'Sum - {sumx}')
            number = sumx
    st.divider()
    if number>0:
        st.subheader(f'Numerology number - {number}')
        print('Numerology number - ',number)
        st.caption(number_character[number])
    else:
        st.caption('Name is empty')
    print()

st.title(":rainbow[Numerology Calculator]")
name = st.text_input('Enter name')
result =  st.button('Calculate', use_container_width = True)

if result == True:
    numerology(name)
