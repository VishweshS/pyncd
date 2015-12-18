import gzip

x = open('1.png', 'rb').read() # file 1 of any type
y = open('2.png', 'rb').read() # file 2 of the same type as file 1
x_y = x + y # the concatenation of files

x_comp = gzip.compress(x) # compress file 1
y_comp = gzip.compress(y) # compress file 2
x_y_comp = gzip.compress(x_y) # compress file concatenated

# print len() of each file
print(len(x_comp), len(y_comp), len(x_y_comp), sep=' ', end='\n')

# magic happens here
ncd = (len(x_y_comp) - min(len(x_comp), len(y_comp))) / max(len(x_comp), len(y_comp))

print(ncd)