class transCookie:
    def __init__(self, cookie) -> None:
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = 'Cookie: uname=190648241; pid=37422; tl=1; lv=2; fid=1976; _uid=107504085; uf=b2d2c93beefa90dcdbf7676745d63affff9b2af18de73f2add7e5c4b773399383b4a201b941b07f7381afe20fd846ad3913b662843f1f4ad6d92e371d7fdf6440a5cf50571bb9ae7fd68be96b6183b1a90eccae084eed2847aa216016ad587f16037342da1e71cd8; _d=1606796315426; UID=107504085; vc=B61985BA180EC0C4DC892ABDD6639B7C; vc2=E83C3B16AA89BDBBCF282FE02DFA8485; vc3=KIzNRuLh%2FtBi5fvviUx%2BhAwAC167arwmIowoZpx2qu6J8s%2BMOpTCAzfeYO07r0tV3%2F4x1tX8XxE4XSiHylfsevyiHgok%2BrQRgtPzKWavYItnN%2FGTL38RatedP2nh8lrT69Qxi4ks%2BHn5DtPB0KvD%2FR5MC7OaqQ7N423vN0ouzkU%3De26fd347fd5e44ef079e6594ab67c02a; xxtenc=80d483b15d3bca19ecc053ee96b0eccb; DSSTASH_LOG=C_38-UN_336-US_107504085-T_1606796315428; fanyamoocs=EE602050CCF8DFF89D9B035A95892A87; thirdRegist=0; k8s=2205e1044b92a06f449a4cb12881c61280016a0a; jrose=2033FD1F0C25BD3A36B584F4A99A4B23.mooc-575182366-1bst7; route=f9c314690d8e5d436efa7770254d0199'
    trans = transCookie(cookie)
    print(trans.stringToDict())



resuit = {
    'Cookie:uname': '190648241',
    'pid': '37422',
    'tl': '1',
    'lv': '2',
    'fid': '1976',
    '_uid': '107504085',
    'uf':'b2d2c93beefa90dcdbf7676745d63affff9b2af18de73f2add7e5c4b773399383b4a201b941b07f7381afe20fd846ad3913b662843f1f4ad6d92e371d7fdf6440a5cf50571bb9ae7fd68be96b6183b1a90eccae084eed2847aa216016ad587f16037342da1e71cd8',
    '_d': '1606796315426',
    'UID': '107504085',
    'vc': 'B61985BA180EC0C4DC892ABDD6639B7C',
    'vc2': 'E83C3B16AA89BDBBCF282FE02DFA8485',
    'vc3':'KIzNRuLh%2FtBi5fvviUx%2BhAwAC167arwmIowoZpx2qu6J8s%2BMOpTCAzfeYO07r0tV3%2F4x1tX8XxE4XSiHylfsevyiHgok%2BrQRgtPzKWavYItnN%2FGTL38RatedP2nh8lrT69Qxi4ks%2BHn5DtPB0KvD%2FR5MC7OaqQ7N423vN0ouzkU%3De26fd347fd5e44ef079e6594ab67c02a',
    'xxtenc': '80d483b15d3bca19ecc053ee96b0eccb',
    'DSSTASH_LOG': 'C_38-UN_336-US_107504085-T_1606796315428',
    'fanyamoocs': 'EE602050CCF8DFF89D9B035A95892A87',
    'thirdRegist': '0',
    'k8s': '2205e1044b92a06f449a4cb12881c61280016a0a',
    'jrose': '2033FD1F0C25BD3A36B584F4A99A4B23.mooc-575182366-1bst7',
    'route': 'f9c314690d8e5d436efa7770254d0199'
}
