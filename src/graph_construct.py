import argparse, json

def merge_json(file, sec, param, value):
  style_prop = {
      "basicPropertyValues": [
        {
          "pred": f"https://w3id.org/kgviz/{param}",
          "val": f"{value}"
        }
      ]
    }

  for f_edge in file["graphs"][0]["edges"]:
    for s_edge in sec["graphs"][0]["edges"]:
      if f_edge["sub"] == s_edge["sub"] and f_edge["pred"] == s_edge["pred"] and f_edge["obj"] == s_edge["obj"]:
        f_edge["meta"] = style_prop

  return file

def main(args):
  f = open(args.input)
  file = json.load(f)
  f = open(args.sec)
  sec = json.load(f)

  output = merge_json(file, sec, args.param, args.value)

  with open(args.output, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input', help='input json file')
  parser.add_argument('sec', help='json with additional relationships')
  parser.add_argument('output', help='output file')
  parser.add_argument('param', help='property name')
  parser.add_argument('value', help='value of the param')
  

  args = parser.parse_args()
  main(args)