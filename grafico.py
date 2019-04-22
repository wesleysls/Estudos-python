import matplotlib.pyplot as plt
x = [1,3,5,7,9]
y = [2,3,7,1,4]

x2 = [2,4,6,8,10]
y2 = [4,1,4,3,5]

plt.title("Meu grafico em python")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

# plt.bar(x,y,label='grupo 1')
# plt.bar(x2,y2,label='grupo 2')
# plt.legend()
plt.scatter(x,y,label="meus pontos")
plt.plot(x,y)
plt.legend()
plt.show()