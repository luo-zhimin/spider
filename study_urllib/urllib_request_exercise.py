import urllib.request
import urllib.parse
import json

# 百度翻译
# methods post
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    'Cookie': 'BAIDUID=E50DACFEAF17F1F7EFC6136939A811A9:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1660055733; BIDUPSID=9BC9B8222FA28C2FEDC83CC1422E04E6; BDUSS=DJpYndrV0t5dTRyLTNtelAwV212aWIwSWw2anNra0JsN0lZZmdCOUFUQ29iU3hqSVFBQUFBJCQAAAAAAQAAAAEAAADACJ8UwuS2~sen5~QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKjgBGOo4ARjT; BDUSS_BFESS=DJpYndrV0t5dTRyLTNtelAwV212aWIwSWw2anNra0JsN0lZZmdCOUFUQ29iU3hqSVFBQUFBJCQAAAAAAQAAAAEAAADACJ8UwuS2~sen5~QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKjgBGOo4ARjT; BDSFRCVID=A58OJexroG0w9T5jdm5auVhdd2KKvV3TDYLEOwXPsp3LGJLVcKvVEG0Pt8lgCZu-2ZlgogKK0eOTHk_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JJkO_D_atKvDqTrP-trf5DCShUFsLUJrB2Q-XPoO3KJbbf-GM4OV3n_03x7bKTjiW5cpoMbgylRp8P3y0bb2DUA1y4vp5MnqQeTxoUJ2fnRJEUcGqj5Ah--ebPRiJPQ9QgbWMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0MC09j6KhDTPVKgTa54cbb4o2WbCQbn4W8pcN2b5oQT8WeJ8tat3L0tjt-Jne5IovOPQKDpOUWfAkXpJvQnJjt2JxaqRCKhv-Sl5jDh3Me-AsLn6te6jzaIvy0hvctn5cShncBUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhjGtOtjDttb3aQ5rtKRTffjrnhPF3hfoDXP6-hnjy3bRfVx-a2JbVEx5G347fb5DUypjpJh3RymJ42-39LPO2hpRjyxv4-UPB34oxJpOJfIJM5McaHCoADb3vbURvD-Lg3-7WyM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE_D0yJD_hhIvPKITD-tFO5eT22-usK2nl2hcHMPoosIJ6eq8hM40DqfvtLtvb5nria-QCtMbUoqRHXnJi0btQDPvxBf7pK23q-q5TtUJMbbRTLp6hqjDlhMJyKMnitIT9-pnoXhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuj6tWj6j0DNRabK6aKC5bL6rJabC3EDK9XU6q2bDeQN3fql0t2DnL_RjaQJnfeKooynj4Dp0vWtv4WbbvLT7johRTWqR4HpvC3xonDh83eMvM3hTtHRrzWn3O5hvvhb5O3M7OBUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRAe_D--3j; BAIDUID_BFESS=E50DACFEAF17F1F7EFC6136939A811A9:FG=1; BDSFRCVID_BFESS=A58OJexroG0w9T5jdm5auVhdd2KKvV3TDYLEOwXPsp3LGJLVcKvVEG0Pt8lgCZu-2ZlgogKK0eOTHk_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=JJkO_D_atKvDqTrP-trf5DCShUFsLUJrB2Q-XPoO3KJbbf-GM4OV3n_03x7bKTjiW5cpoMbgylRp8P3y0bb2DUA1y4vp5MnqQeTxoUJ2fnRJEUcGqj5Ah--ebPRiJPQ9QgbWMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0MC09j6KhDTPVKgTa54cbb4o2WbCQbn4W8pcN2b5oQT8WeJ8tat3L0tjt-Jne5IovOPQKDpOUWfAkXpJvQnJjt2JxaqRCKhv-Sl5jDh3Me-AsLn6te6jzaIvy0hvctn5cShncBUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhjGtOtjDttb3aQ5rtKRTffjrnhPF3hfoDXP6-hnjy3bRfVx-a2JbVEx5G347fb5DUypjpJh3RymJ42-39LPO2hpRjyxv4-UPB34oxJpOJfIJM5McaHCoADb3vbURvD-Lg3-7WyM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE_D0yJD_hhIvPKITD-tFO5eT22-usK2nl2hcHMPoosIJ6eq8hM40DqfvtLtvb5nria-QCtMbUoqRHXnJi0btQDPvxBf7pK23q-q5TtUJMbbRTLp6hqjDlhMJyKMnitIT9-pnoXhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuj6tWj6j0DNRabK6aKC5bL6rJabC3EDK9XU6q2bDeQN3fql0t2DnL_RjaQJnfeKooynj4Dp0vWtv4WbbvLT7johRTWqR4HpvC3xonDh83eMvM3hTtHRrzWn3O5hvvhb5O3M7OBUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRAe_D--3j; delPer=0; BDRCVFR[d9MwMhSWl4T]=mk3SLVN4HKm; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1679065029; BDRCVFR[feWj1Vr5u3D]=UhzBld-0LXCuvqEuvk-QhPEUi4Cps; BDRCVFR[fb3VbsUruOn]=ddONZc2bo5mfAF9pywdpAqVuNqsus; BA_HECTOR=01052k2gagah210g8kak2k7u1i3ksoo1n; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; rsv_i=1eefWB2oOER3IENeTZL34w73KhuPRFHGofWhYcsDiqkSwRAG8tOCsas2nlKtOmUBQ+kd4+JlWnm7T3xYJb/yJujw3zYpqiQ; SE_LAUNCH=5:28026094_16:28026094; H_WISE_SIDS=219946_234020_219559_216837_219943_213038_230288_110085_236308_243872_244256_244714_240590_245411_248170_243706_249060_232280_247147_250738_250888_249340_252005_252580_247390_247585_253175_234295_253066_253465_203519_248437_253705_244956_253516_253427_254322_253321_254422_254473_179346_254591_252644_254268_254729_250606_248124_250225_254749_251133_236538_253212_255288_253693_250390_251618_255482_255653_252129_255936_255956_234484_255890_251442_107313_256062_256095_256093_255679_248697_256127_253152_256083_255803_253990_256011_256259_255661_256278_256296_256315_254833_251058_256321_256350_229154_255176_256395_245042_253900_256223; PSINO=5; H_WISE_SIDS_BFESS=219946_234020_219559_216837_219943_213038_230288_110085_236308_243872_244256_244714_240590_245411_248170_243706_249060_232280_247147_250738_250888_249340_252005_252580_247390_247585_253175_234295_253066_253465_203519_248437_253705_244956_253516_253427_254322_253321_254422_254473_179346_254591_252644_254268_254729_250606_248124_250225_254749_251133_236538_253212_255288_253693_250390_251618_255482_255653_252129_255936_255956_234484_255890_251442_107313_256062_256095_256093_255679_248697_256127_253152_256083_255803_253990_256011_256259_255661_256278_256296_256315_254833_251058_256321_256350_229154_255176_256395_245042_253900_256223; ab_sr=1.0.1_MDMwNTgxMThjMGViZWM4MzY1OTE1ODdlNDkwZTNhZGVhMGU1M2M5MDZhODMzMmI4OGI1M2Q2ZTdkNjk1MGRlY2Q0ODljNTY0OGExY2UxMDgzOTJiNDUwNzQyYTU5MTIyZGNhNGU3ZDRjZjRiMjdjOTg2NWE1ZDZiOTkyYTQ0ZTgyNjdhNjA4M2FiNWQ3ZTZlOTFjMDNiNWE2MWNhY2YxYWQ1NjZmMmU5ZGYwNzE3YWIyMzBhZWNkM2FhNDNhNmM0',
    # 'Acs-Token': '1681614611198_1681614703361_pYCi8wqXuFtZAwneIfZQPvhK6jHrJoaP3F/bENvYy2hZ6YIJ1tKpeipJYbbIw3Sg7GD4KGuOeRoR0W2iKV/iWyMathdV4jQzBvVv+MDOpcXpoWzohOKylVlkVR6eVfA4WHMK1GSRotYezfdQ+YBv4R4W1DSYXIZtEOWsi/Nb2Vt+NwhJxODRChRqJ7zmFy2zboIgfO6o793Rq3KReV4cdWDZEzwr3ldGQaw03NoDpyhX2Iq+zfEzhrVpa6mVF0GspHC7oDLKJrk7tklas3d6X6nDInIOXLOzlbeteEFYeduR3nRQTu+dNd4OIzhKsnH6AJThnLkUlZDP3RyMmn92/Wiw3SvXw96+da1INjLcjlWiyCbxz39LHdLCUjYCB801BbU6dyRZ7H5vFn0xDK8/SI7Tum889UjAa7kgtv1PHRW1iwNYSAnR0Uwm9E8ve3utLGgb1PubeSlZRk2bZ0OVyhNgcFUAqcl/9YCDzST28Run0nryzYf8r13H1a1+g0qG',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept': '*/*',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '139',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Host': 'fanyi.baidu.com',
    # 'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': 'macOS',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'different',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '875047.637206',
    'token': '1d8323025108a9f3aa74185601007084',
    'domain': 'common'
}

# 先处理data
data = urllib.parse.urlencode(data).encode('utf-8')

# 定制请求
request = urllib.request.Request(url=url, data=data, headers=headers)

# 发送请求
response = urllib.request.urlopen(request)

# 接收返回数据
content = response.read().decode('utf-8')

# 解析数据
content = json.loads(content)

print(content)
