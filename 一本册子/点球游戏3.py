'''
    更新内容：

        如果是平局，则继续进行PK

'''




from random import choice


def kick():
    print '点球游戏开始...\n'

    yourScore = 0
    computerScore = 0

    for i in range(6):
        print '==== Round %d - You Kick! ====' % (i+1)

        print 'Choose your side to shoot:'

        print 'left, center, right'

        youChoose = input()

        print 'You choose: ' + youChoose

        l = ['left', 'center', 'right']

        computerChoose = choice(l)

        print 'Computer choose: ' + computerChoose

        if youChoose == computerChoose:
            computerScore+=1
        else:
            yourScore+=1

    print 'Game Over, Your Score = %d, Commputer Score = %d ' % (yourScore,computerScore)
    
    if yourScore > computerScore:
        print 'You Win!'
    elif yourScore < computerScore:
        print 'Computer Win!'
    else:
        print '\ndogfall, Again!\n'
        kick()



kick()
