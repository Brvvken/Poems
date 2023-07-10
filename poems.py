while True:
    print('''           ____
          |  _ \    ___     ___   _ __ ___    ___ 
          | |_) |  / _ \   / _ \ | '_ ` _ \  / __|
          |  __/  | (_) | |  __/ | | | | | | \__ \ 
          |_|      \___/   \___| |_| |_| |_| |___/ 
    ''')

    print(''' 
    ''')
    print("1. Sonnet")
    print("2. Villanelle")
    print("3. Haiku")
    print("4. Ekphrastic")
    print(" ")
    print("More will be added soon....")

    print(''' 
    ''')
    print("Which poem would you like to see an example of? (Enter 'q' to quit)")

    choose = input("Choose (1/2/3/4): ")

    if choose == "1":
        print(" ")
        print("Here is an example of a Sonnet poem:")
        print(" ")
        print('''How do I love thee? Let me count the ways
        I love thee to the depth and breadth and height 
        My soul can reach, when feeling out of sight 
        For the ends of being and ideal grace. 
        I love thee to the level of every day's
        Most quiet need, by sun and candlelight.
        I love thee freely, as men strive for right;
        I love thee purely, as they turn from Praise.
        I love with a passion put to use
        In my old griefs, and with my childhood's faith.
        I love thee with a love I seemed to lose
        With my lost saints, I love thee with the breath,
        Smiles, tears, of all my life! and, if God choose,
        I shall but love thee better after death.

        -Elizabeth Barrett Browning 
        ''')

    elif choose == "2":
        print("Here is an example of a Villanelle poem:")
        print('''I have lost my turtledove:
        Isn't that her gentle coo?
        I will go and find my love.

        Here you mourn your mated love;
        Oh, God—I am mourning too:
        I have lost my turtledove.

        If you trust your faithful dove,
        Trust my faith is just as true;
        I will go and find my love.

        Plaintively you speak your love;
        All my speech is turned into
        "I have lost my turtledove."

        Such a beauty was my dove,
        Other beauties will not do;
        I will go and find my love.

        Death, again entreated of,
        Take one who is offered you:
        I have lost my turtledove;
        I will go and find my love.
        ''')

    elif choose == "3":
        print("Here is an example of a Haiku poem:")
        print(" ")
        print('''I write, erase, rewrite
        Erase again, and then
        A poppy blooms.

        -Katsushika Hokusai
        ''')

    elif choose == "4":
        print("Here is an example of an Ekphrastic poem:")
        print(" ")
        print('''What men or gods are these? What maidens loth?
        What mad pursuit? What struggle to escape?
        What pipes and timbrels? What wild ecstasy?

        Heard melodies are sweet, but those unheard
        Are sweeter; therefore, ye soft pipes, play on;
        Not to the sensual ear, but, more endear’d,
        Pipe to the spirit ditties of no tone:
        Fair youth, beneath the trees, thou canst not leave
        Thy song, nor ever can those trees be bare;
        Bold Lover, never, never canst thou kiss,
        Though winning near the goal yet, do not grieve;
        She cannot fade, though thou hast not thy bliss,
        For ever wilt thou love, and she be fair!

        Ah, happy, happy boughs! that cannot shed
        Your leaves, nor ever bid the Spring adieu;
        And, happy melodist, unwearied,
        For ever piping songs for ever new
        ''')

    elif choose.lower() == "q":
        break

    else:
        print("Invalid choice. Please choose again.\n")