import json

input = '''
21 >>> ぼくらのニコニコがいちばんだ
22 >>> 【UTAUカバー・MMD】カガリビト【波音リツキレ音源・ニコカラ】
23 >>> 辻野あかりの激唱
24 >>> 【オリ曲】Summer goes by 逆音セシル　　　　　　by ____natural
25 >>> 石雨アイド「Monochrome」UTAUオリジナル曲
26 >>> 忘れないで
27 >>> 落陽に寄せる - 椎音あま
28 >>> 【UTAUカバー】 ヒウマノイドズヒウマニズム 【欲音ルコ♀】
29 >>>> sm36974825 >>>> ネギドリル】い～あるふぁんくらぶ（中文）【MMD・らぶ式】
30 >>>> sm36918763 >>>> Mu Telescopii _ 旭音エマ
【闇音レンリ】Liselotte【オリジナル】
'''

output = json.dumps(input).split('\\n')

for oo in output: print(oo)

