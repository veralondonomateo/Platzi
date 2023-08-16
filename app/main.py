import mod
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv')
  desition = input('De que país deseas conocer los datos => ').lower()
  result = mod.list_by_country(data,desition)

  if len(result) > 0:
    desition = result[0]
    keys, values = mod.get_population()
    charts.generate_pie_chart(keys,values)
  

  
  
  print(result)

if __name__ == '__main__':
  run()