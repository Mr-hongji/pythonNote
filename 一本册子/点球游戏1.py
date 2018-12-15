print '点球游戏开始...\n'

print 'Choose one side to shoot:'

print 'left, center, right'

youChoose = input()

print 'You Choose: ' + youChoose

l = ['left', 'center', 'right']

from random import choice

computerChoose = choice(l)

print 'Computer Choose: ' + computerChoose

if youChoose != computerChoose:
    print 'Goal！' #得分
else:
    print 'Oops...' #叹息
    



