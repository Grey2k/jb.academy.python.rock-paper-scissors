# Write your code here
pick = input().strip()

contra = None

if pick == 'rock':
    contra = 'paper'
if pick == 'paper':
    contra = 'scissors'
if pick == 'scissors':
    contra = 'rock'

print(f'Sorry, but the computer chose {contra}')
