#...........................python 3.........................................
import csv

class Item:
	def __init__(self, site, classificacao):
		self.site = site
		self.classificacao = classificacao

arquivo = open('SitesDesordenados_20190405211608.csv')
linhas = csv.reader(arquivo)
arr = []

for linha in linhas:
	site = linha[0].split(";")
	arr = arr + [Item(site[0],site[1])]


def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves
		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i].classificacao < R[j].classificacao: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i].classificacao+" "+arr[i].site,end=" ")
		print() 

mergeSort(arr)
printList(arr)


arquivo = csv.writer(open("SitesOrdenados.csv", "w", newline=''))
for linha in arr:
	arquivo.writerow([linha.site+";"+linha.classificacao])