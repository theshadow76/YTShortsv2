import requests
import json

url = 'https://studio.youtube.com/youtubei/v1/upload/createvideo?alt=json&key=AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo'

headers = {
    'authority': 'studio.youtube.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'SAPISIDHASH 1703261649_894cf9532978718d009a82cc83816981a694d18c',
    'content-type': 'application/json',
    'cookie': 'VISITOR_INFO1_LIVE=MSzsLXzeR3k; _gcl_au=1.1.1815493779.1698415892; [other cookies truncated for brevity]',
    'origin': 'https://studio.youtube.com',
    'referer': 'https://studio.youtube.com/channel/UCpPx_JYfFu5EhclRtRck54A/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.118 Safari/537.36',
    'x-goog-authuser': '5',
    'x-goog-visitor-id': 'CgtNU3pzTFh6ZVIzayiZ65asBjIKCgJDTBIEGgAgVQ%3D%3D',
    'x-origin': 'https://studio.youtube.com',
    'x-youtube-ad-signals': 'dt=1703261594155&flash=0&frm&u_tz=-180&u_his=4&u_h=1050&u_w=1680&u_ah=946&u_aw=1680&u_cd=30&bc=31&bih=841&biw=1072&brdim=0%2C25%2C0%2C25%2C1680%2C25%2C1680%2C946%2C1072%2C841&vis=1&wgl=true&ca_type=image',
    'x-youtube-client-name': '62',
    'x-youtube-client-version': '1.20231219.01.00',
    'x-youtube-delegation-context': 'EhhVQ3BQeF9KWWZGdTVFaGNsUnRSY2s1NEEqAggI',
    'x-youtube-page-cl': '592271021',
    'x-youtube-page-label': 'youtube.studio.web_20231219_01_RC00',
    'x-youtube-time-zone': 'America/Santiago',
    'x-youtube-utc-offset': '-180',
}

data = {"channelId":"UCpPx_JYfFu5EhclRtRck54A","resourceId":{"scottyResourceId":{"id":"ACKujmzU5l7PCfHXHykHhkiJ7HgxegW/IZKqLclGBI+SAk8z9jyjG1GLXyjdT3Rig9HAgnzCfnwou7nQECfLMdRRkvcG1bEINKtun8+NGrdTBrutRBC3IvO0m0iI7FHcJvmuBtOhTzaLOQht0qM2gQRgGMMDjEM5wBFVH8LIpgBtAcVESSQjScqvmPH4wptXofu+yhWIsxFYeJRCY7p9BHmSj4F4VvYQ0wKKairXTZlHXkIK1tPlukwo0PZpssBcB0Vf/jYNJ7JKrw6rbAOsGWz5eX2b5jBrzWhSM0Rt2e9YvIJAq+QO7wD+5jIOISVLNjpqMwdO0xy/eh5KjDXFGoyMmG1qF9xZAJIN31lrRvdfGWePtCnG4jY="}},"frontendUploadId":"innertube_studio:25D6BFB3-EDCF-4D9C-BDAA-4BD70AF181BE:0","initialMetadata":{"title":{"newTitle":"output video2"},"privacy":{"newPrivacy":"PRIVATE"},"draftState":{"isDraft":True}},"context":{"client":{"clientName":62,"clientVersion":"1.20231219.01.00","hl":"es-419","gl":"CL","experimentsToken":"","utcOffsetMinutes":-180,"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","screenWidthPoints":1072,"screenHeightPoints":841,"screenPixelDensity":2,"screenDensityFloat":2},"request":{"returnLogEntry":True,"internalExperimentFlags":[],"eats":"AcIjWyHZN87WJpzDO6vUqkfmbe5-kzhIIJvSOk_7BxQKIE3mvMs3t4Jq9qm9qv_rbVFlAxomOASgP7Rrg3td18ZS1Txho4oqYw8X2a6Krs0JGq_4J8QgMAPBC1PKyg==","attestationResponseData":{"challenge":"a=6&a2=10&b=FoHX4_YgohpLXWBaG4DE6uxn0R0&c=1703261599&d=62&t=7200&c1a=1&x4=1&hh=185qqtHwNXJrank3cNWKMhFodrA2rtwtFJjLe95-iKg","webResponse":"$HIM5g9tRAAbViGfY9Yje4errFxDD4e6nADQBEArZ1NsV1wSrIlZwe7HVLta9LTgF4WNAUu_dCknt-eFa6QVnPfd8UNd9CDV1_x3TFdPangAAAHXOAAAATPQBBwUIOttuxJGcleTxMpbS8OK5OX6bY6210K9NAbL56wtFr1nvsoycEhnPukq1UA5HhyR_7JA9xDTnYhlxPPYTFfL-UOsGIminc8s7T-gfm7Im0myNNCe0Xi2El7aXMmUhjhNpcugSp065U3-revjRaGyIodZjLeaJtxVVAqAZhj2gPgHFPPfHvBqeYyD6S92yf5tcHnR3TdVd5Tl3sB41f3_RBJNdhFKgrEt-jgvL3zX5UkiHQEl-zq6GEgtVvd1tWZWBmPz5bxWv48lgU4AxZQ3jHWvwMUXamlBoBbnFEvr-Ei7hme1b6hImzdim2xCaBaaJckAlrDhP75e1m_HRLBIQn9wE5itrIm9M8_4hsSmAZcLApMBLnldBs0DxXmHgq8F8oP1LaQol1-kdvYqqGVO-FThV38lISn_UTqrA_W7KgyEQ_woye1f2wPK4SamjeEzCgdq8cmGJN8WDphATqxS6FV3xv_UjZ9SiR3VY1fCMC63647_qUXG8ectLP-YSm832HkU5YIWC6NlVvRQfb0tYl1VDaHC644ut0e4CcbMwXf9hI1TAvTo-Wflcdq_pY7AiqGR_sgS31VlA1CCSGZn3HzGlz9HrpMjEJkjRl-c_hElFHB_3FuGvkqQSTmg4YCSCXrzhSjLiPGD-x9MGpyrUp6Rolzvd5mdIa17LH2EJBFA2SpZY_5PAFrmCxi8wDafW9LSUNroiA3bnTGxdqQpIpg8Q3J765Zf2BXE1Uw-6tl1RsQZrzc4HxxiZS3eBiLDBVGmy5KYnYIq3vl-9De59b7r6wOP1nXuagwPDxfn1-tnR0IB-f77U7QUdj2_jpitgsRt5vXynDXDfSZHJ2TVq_bNR8ji-4WSKhXnJ2b5Rh9vJgAD5pFV_NBaSuTxtYTguN6HlA25rbrLZT0tFEtI19pNIS9BzCAGH24sX6jX4t4Ez-kHA25-ocm2c4kAHlu5-MjeBPMIloQiILATrVEfofSFuH-492duHc3Yu5kbZeX0RMcHFapLXP6vPW0XkuELxfvWjv6iNJnpuhd1tZtUjIX4zUhs-hwGuAlET4BB3Cp7iLPBWgPrn_kuv1MJ38GkFEADwhMOw2VD3ynqp1h3IKjmCUP3YDV7pKZs6KIckdJD5AFLVhTpMI404XesCihyVo1IlU8JG2fTZZkgd4mGWJV6RQLIfV--P81RlU3HfWVYzJBDL0_TKeez3C4x8YIm63aAZfCkOD1fWGgYrYCkhXHNQPzKmYFaouUC_mkXc_B_BHmywxhv6CYUrzxMdb3UrWtGvUjSQpWMRNqDQFuJ1jrDOSLhT3Ke9IZ141llNe_I0ea5bQ7bJ4uSraQGAEQBklSOBrCvg6H4eV4pGWDhXQAWxtWH8ALC-eoHlsZLBpFeh2yuCxyhgzb1W8uFTmmfBt5NyHO9c6SWaxrYGOqvJOdThrLYQanZhBR6NgFAECuCfAKpWnCMu2NyJsBNt0QNbCNCCmK1zadbnC0p-JdRI9YWT67jOpJm6H1z-QWNONoKltzGpYVA6IXLCIxRMKbiYei84nj_hnkvhfR_zWubkLDkM8Vnaa6D8mdyA-ov3l6w-DbUu2q1Z_8hUjXM999h2Wu56s78iXDJWYX-IJN9RCGF-RY3Mdt_mKFubztQOLC9_4VgMwuVIgzV7MYf-a1yose14S1mHkREYe0Yfg6CmsxQl8DkASsQB0lJ0TEHdJ9R5Rr13pogkoRVMO541uTR_uCtD38A0hPEMW6gkkTWaGrc_R7hg3A-rS67NCQPO9IN5kibdeKWxdLIWHABS-bAjOgYcnvER8SuP4PPHpU6bRTEY66W6xmjl4MUjOFgRQqyRDSI9RmA4FoZR_cmLsozA0SnkrRdAdBfe0RDVqyKZ2YIY3xI6hlNVNEpxHOFFxE01CWFNDEN22z9wWgOm8G4GAdcZj0bxi1UOna02sWtLROOx_6TKlBvvVHlnvjo6hSAPFTdnxugM6etZxn0reJBe3oPtN12NSZgI2fHcef1lApuMGvxq1g3eajqv8RvL3pnOoP8Ug7Hhf-E5GsQUIhK5IqhVBkZ3Sl52ADxXkEBQhCFRDaoNki6lA1KJKS4eCyHApoTpK4J_whzvp_aypK9AbLQ8zdfPDtPHPbuyyRlF54P1XpeEXNd6VgxzVlFFFFKc5S5brBc210aQ4JFWavYeDfOk2B9ADDB8d9jlTWrYnks2jXMG4W7zPzduaXQgsg_A6OBHQ-KBInIbEKoTqcnFbhHN9-g-6sn1msNz-yfe2WIv5suoCnpxqcc_fkuWFYr3tz2uSs_n-pVyYT1exhmioy_VKrryXHzo_m7J4dWKLhjV4sqHlIJgDXeKFeo8xcv3cSipsohbtcMC_A4HglqOcVvKQNTLZeix3DUN8xrz_w-gbJmoncQu2hQzmn98YMQ_HvCKChkIOjke09X0LM1uoEjmBZ9N_IBJS_jsLEEJ5C-iKfPQ9NHVttBm-pFBXHCWrpOrwKU1VqvnnSivS5jFTXFnnZ2KYfyP7MMPlCfCvW7h4hlk4ZbdHjWnJIeBPHTs9T_V5E9RRMnK4WsBRALpnRwl008fNDt1UWuEAcRZZafuAyZ8DKEpu9Jdw9PHQNpGiDbGwYEIgKCVQvUJApyN-J8kqwiLbss5R8h9TDQXqews-Gca6_MN2u1OOC8d1Ip2q9A7M0rdEa8tI1C9fWhAfCDf9OOPnUOUzZRqJ5CELs1TXgiCyxN4UtfghJSx5pmEmWwhIfgtM2zugtmxIaj7vv39Ua1rSqIRZa3rqQXLkguBOC195MaM-243WHA0RMJOlYgSks9IXpq1SQ"},"sessionInfo":{"token":"AWS8b1vfM503AuUY5D-s2L_CBg-01vTV6lCYkGUkzmblmS0GriL2yX25KS-sbyi9QG8qZCtpeTAGp5aFkazAD4Wcjs7tWF2JOYzIi_gmj9-q2AYYwDsYE0bRZPianq1nznACP0n7zDYNyTv_lasqVq2pjruHqKbN9pQ="},"consistencyTokenJars":[]},"user":{"delegationContext":{"externalChannelId":"UCpPx_JYfFu5EhclRtRck54A","roleType":{"channelRoleType":"CREATOR_CHANNEL_ROLE_TYPE_OWNER"}},"serializedDelegationContext":"EhhVQ3BQeF9KWWZGdTVFaGNsUnRSY2s1NEEqAggI"},"clientScreenNonce":"MC45MjYxOTE1MzkxOTExMTk3"},"delegationContext":{"externalChannelId":"UCpPx_JYfFu5EhclRtRck54A","roleType":{"channelRoleType":"CREATOR_CHANNEL_ROLE_TYPE_OWNER"}},"presumedShort":True}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
