#2.1
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
#print(codes)


#2.2
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
#print(codes)

#2.3
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
#beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
#print(beyond_ascii)