<template>
  <el-cascader
  :options="options"
  change-on-select
></el-cascader>
</template>

<script>
  export default {
    data() {
      return {
        options: [{
          value: '西南地区',
          label: '西南地区',
          children: [{
            value: '西藏',
            label: '西藏',
            children: [{
              value: '灵芝 270',
              label: '灵芝 270'
            }, {
              value: '昌都 269',
              label: '昌都 269'
            }, {
              value: '拉萨 268',
              label: '拉萨 268'
            }]
          }, {
            value: '云南',
            label: '云南',
            children: [{
              value: '蒙自 267',
              label: '蒙自 267'
            }, {
              value: '勐腊 266',
              label: '勐腊 266'
            }, {
              value: '元江 265',
              label: '元江 265'
            }, {
              value: '思茅 264',
              label: '思茅 264'
            }, {
              value: '澜沧 263',
              label: '澜沧 263'
            }, {
              value: '临沧 262',
              label: '临沧 262'
            }, {
              value: '昆明 261',
              label: '昆明 261'
            }, {
              value: '楚雄 260',
              label: '楚雄 260'
            }, {
              value: '腾冲  259',
              label: '腾冲  259'
            }, {
              value: '丽江 258',
              label: '丽江 258'
            }, {
              value: '德钦 257',
              label: '德钦 257'
            }]
          }, {
            value: '贵州',
            label: '贵州',
            children: [{
              value: '兴义 256',
              label: '兴义 256'
            }, {
              value: '三穗 255',
              label: '三穗 255'
            }, {
              value: '贵阳 254',
              label: '贵阳 254'
            }, {
              value: '遵义 253',
              label: '遵义 253'
            }, {
              value: '毕节 252',
              label: '毕节 252'
            }, {
              value: '桐梓  251',
              label: '桐梓  251'
            }, {
              value: '威宁 250',
              label: '威宁 250'
            }]
          }, {
            value: '重庆',
            label: '重庆',
            children: [{
              value: '酉阳 249',
              label: '酉阳 249'
            }, {
              value: '重庆沙坪坝 248',
              label: '重庆沙坪坝 248'
            }]
          }, {
            value: '四川',
            label: '四川',
            children: [{
              value: '泸州 247',
              label: '泸州 247'
            }, {
              value: '南充 246',
              label: '南充 246'
            }, {
              value: '万源 245',
              label: '万源 245'
            }, {
              value: '会理 244',
              label: '会理 244'
            }, {
              value: '西昌 243',
              label: '西昌 243'
            }, {
              value: '宜宾 242',
              label: '宜宾 242'
            }, {
              value: '九龙 241',
              label: '九龙 241'
            }, {
              value: '乐山 240',
              label: '乐山 240'
            }, {
              value: '成都 239',
              label: '成都 239'
            }, {
              value: '理塘 238',
              label: '理塘 238'
            }, {
              value: '绵阳 237',
              label: '绵阳 237'
            }, {
              value: '松潘 236',
              label: '松潘 236'
            }, {
              value: '红原 235',
              label: '红原 235'
            }, {
              value: '马尔康 234',
              label: '马尔康 234'
            }, {
              value: '甘孜 233',
              label: '甘孜 233'
            }]
          }]
        }, {
          value: '西北地区',
          label: '西北地区',
          children: [{
            value: '新疆',
            label: '新疆',
            children: [{
              value: '哈密 232',
              label: '哈密 232'
            }, {
              value: '民丰 231',
              label: '民丰 231'
            }, {
              value: '和田 230',
              label: '和田 230'
            }, {
              value: '莎车 229',
              label: '莎车 229'
            }, {
              value: '若羌 228',
              label: '若羌 228'
            }, {
              value: '铁干里克 227',
              label: '铁干里克 227'
            }, {
              value: '巴楚 226',
              label: '巴楚 226'
            }, {
              value: '喀什 225',
              label: '喀什 225'
            }, {
              value: '库车 224',
              label: '库车 224'
            }, {
              value: '阿克苏 223',
              label: '阿克苏 223'
            }, {
              value: '吐鲁番 222',
              label: '吐鲁番 222'
            }, {
              value: '焉耆 221',
              label: '焉耆 221'
            }, {
              value: '乌鲁木齐 220',
              label: '乌鲁木齐 220'
            }, {
              value: '伊宁 219',
              label: '伊宁 219'
            }, {
              value: '乌苏 218',
              label: '乌苏 218'
            }, {
              value: '精河 217',
              label: '精河 217'
            }, {
              value: '克拉玛依 216',
              label: '克拉玛依 216'
            }, {
              value: '和布克赛尔 215',
              label: '和布克赛尔 215'
            }, {
              value: '塔城 214',
              label: '塔城 214'
            }, {
              value: '富蕴 213',
              label: '富蕴 213'
            }, {
              value: '阿勒泰 212',
              label: '阿勒泰 212'
            }]
          }, {
            value: '宁夏',
            label: '宁夏',
            children: [{
              value: '固原 211',
              label: '固原 211'
            }, {
              value: '盐池 210',
              label: '盐池 210'
            }, {
              value: '银川 209',
              label: '银川 209'
            }]
          }, {
            value: '青海',
            label: '青海',
            children: [{
              value: '囊谦 208',
              label: '囊谦 208'
            }, {
              value: '达日 207',
              label: '达日 207'
            }, {
              value: '玛多 206',
              label: '玛多 206'
            }, {
              value: '玉树 205',
              label: '玉树 205'
            }, {
              value: '曲麻莱 204',
              label: '曲麻莱 204'
            }, {
              value: '托托河 203',
              label: '托托河 203'
            }, {
              value: '兴海 202',
              label: '兴海 202'
            }, {
              value: '民和 201',
              label: '民和 201'
            }, {
              value: '西宁 200',
              label: '西宁 200'
            }, {
              value: '都兰 199',
              label: '都兰 199'
            }, {
              value: '格尔木 198',
              label: '格尔木 198'
            }, {
              value: '刚察 197',
              label: '刚察 197'
            }, {
              value: '大柴旦 196',
              label: '大柴旦 196'
            }, {
              value: '冷湖 195',
              label: '冷湖 195'
            }]
          }, {
            value: '甘肃',
            label: '甘肃',
            children: [{
              value: '天水 194',
              label: '天水 194'
            }, {
              value: '武都 193',
              label: '武都 193'
            }, {
              value: '岷县 192',
              label: '岷县 192'
            }, {
              value: '合作 191',
              label: '合作 191'
            }, {
              value: '西峰镇 190',
              label: '西峰镇 190'
            }, {
              value: '平凉 189',
              label: '平凉 189'
            }, {
              value: '榆中 188',
              label: '榆中 188'
            }, {
              value: '兰州 187',
              label: '兰州 187'
            }, {
              value: '乌鞘岭 186',
              label: '乌鞘岭 186'
            }, {
              value: '民勤 185',
              label: '民勤 185'
            }, {
              value: '酒泉 184',
              label: '酒泉 184'
            }, {
              value: '玉门镇 183',
              label: '玉门镇 183'
            }, {
              value: '敦煌 182',
              label: '敦煌 182'
            }]
          }, {
            value: '陕西',
            label: '陕西',
            children: [{
              value: '安康 181',
              label: '安康 181'
            }, {
              value: '汉中 180',
              label: '汉中 180'
            }, {
              value: '西安 179',
              label: '西安 179'
            }, {
              value: '洛川 178',
              label: '洛川 178'
            }, {
              value: '延安 177',
              label: '延安 177'
            }, {
              value: '绥德 176',
              label: '绥德 176'
            }, {
              value: '定边 175',
              label: '定边 175'
            }, {
              value: '榆林 174',
              label: '榆林 174'
            }]
          }]
        }, {
          value: '华南地区',
          label: '华南地区',
          children: [{
            value: '海南',
            label: '海南',
            children: [{
              value: '琼海 173',
              label: '琼海 173'
            }, {
              value: '东方 172',
              label: '东方 172'
            }, {
              value: '海口 171',
              label: '海口 171'
            }]
          }, {
            value: '广西',
            label: '广西',
            children: [{
              value: '钦州 170',
              label: '钦州 170'
            }, {
              value: '灵山 169',
              label: '灵山 169'
            }, {
              value: '南宁 168',
              label: '南宁 168'
            }, {
              value: '龙州 167',
              label: '龙州 167'
            }, {
              value: '梧州 166',
              label: '梧州 166'
            }, {
              value: '桂平 165',
              label: '桂平 165'
            }, {
              value: '百色 164',
              label: '百色 164'
            }, {
              value: '都安 163',
              label: '都安 163'
            }, {
              value: '河池 162',
              label: '河池 162'
            }, {
              value: '桂林 161',
              label: '桂林 161'
            }]
          }, {
            value: '广东',
            label: '广东',
            children: [{
              value: '电白 160',
              label: '电白 160'
            }, {
              value: '阳江 159',
              label: '阳江 159'
            }, {
              value: '汕尾 158',
              label: '汕尾 158'
            }, {
              value: '汕头 157',
              label: '汕头 157'
            }, {
              value: '增城 156',
              label: '增城 156'
            }, {
              value: '河源 155',
              label: '河源 155'
            }, {
              value: '广州 154',
              label: '广州 154'
            }, {
              value: '韶关 153',
              label: '韶关 153'
            }, {
              value: '南雄 152',
              label: '南雄 152'
            }]
          }]
        }, {
          value: '华东地区',
          label: '华东地区',
          children: [{
            value: '江西',
            label: '江西',
            children: [{
              value: '南城 151',
              label: '南城 151'
            }, {
              value: '玉山 150',
              label: '玉山 150'
            }, {
              value: '南昌 149',
              label: '南昌 149'
            }, {
              value: '景德镇 148',
              label: '景德镇 148'
            }, {
              value: '赣州 147',
              label: '赣州 147'
            }, {
              value: '遂川 146',
              label: '遂川 146'
            }, {
              value: '吉安 145',
              label: '吉安 145'
            }, {
              value: '宣春 144',
              label: '宣春 144'
            }]
          }, {
            value: '福建',
            label: '福建',
            children: [{
              value: '厦门 143',
              label: '厦门 143'
            }, {
              value: '崇武 142',
              label: '崇武 142'
            }, {
              value: '永安 141',
              label: '永安 141'
            }, {
              value: '上杭 140',
              label: '上杭 140'
            }, {
              value: '福州 139',
              label: '福州 139'
            }, {
              value: '南平 138',
              label: '南平 138'
            }, {
              value: '建瓯 137',
              label: '建瓯 137'
            }]
          }, {
            value: '安徽',
            label: '安徽',
            children: [{
              value: '屯溪 136',
              label: '屯溪 136'
            }, {
              value: '安庆 135',
              label: '安庆 135'
            }, {
              value: '合肥 134',
              label: '合肥 134'
            }, {
              value: '桐城 133',
              label: '桐城 133'
            }, {
              value: '霍山 132',
              label: '霍山 132'
            }, {
              value: '蚌埠 131',
              label: '蚌埠 131'
            }, {
              value: '寿县 130',
              label: '寿县 130'
            }, {
              value: '亳州 129',
              label: '亳州 129'
            }]
          }, {
            value: '浙江',
            label: '浙江',
            children: [{
              value: '洪家 128',
              label: '洪家 128'
            }, {
              value: '温州 127',
              label: '温州 127'
            }, {
              value: '衢州 126',
              label: '衢州 126'
            }, {
              value: '定海 125',
              label: '定海 125'
            }, {
              value: '杭州 124',
              label: '杭州 124'
            }]
          }, {
            value: '江苏',
            label: '江苏',
            children: [{
              value: '吕泗 123',
              label: '吕泗 123'
            }, {
              value: '东台 122',
              label: '东台 122'
            }, {
              value: '南京 121',
              label: '南京 121'
            }, {
              value: '淮阴（清江） 120',
              label: '淮阴（清江） 120'
            }, {
              value: '赣榆 119',
              label: '赣榆 119'
            }, {
              value: '徐州 118',
              label: '徐州 118'
            }]
          }, {
            value: '上海',
            label: '上海',
            children: [{
              value: '上海 117',
              label: '上海 117'
            }]
          }, {
            value: '山东',
            label: '山东',
            children: [{
              value: '莒县 116',
              label: '莒县 116'
            }, {
              value: '兖州 115',
              label: '兖州 115'
            }, {
              value: '潍坊 114',
              label: '潍坊 114'
            }, {
              value: '济南 113',
              label: '济南 113'
            }, {
              value: '朝阳 112',
              label: '朝阳 112'
            }, {
              value: '成山头 111',
              label: '成山头 111'
            }, {
              value: '龙口 110',
              label: '龙口 110'
            }, {
              value: '惠民县 109',
              label: '惠民县 109'
            }]
          }]
        }, {
          value: '华中地区',
          label: '华中地区',
          children: [{
            value: '湖南',
            label: '湖南',
            children: [{
              value: '常宁 108',
              label: '常宁 108'
            }, {
              value: '零陵 107',
              label: '零陵 107'
            }, {
              value: '武冈 106',
              label: '武冈 106'
            }, {
              value: '株洲 105',
              label: '株洲 105'
            }, {
              value: '芷江 104',
              label: '芷江 104'
            }, {
              value: '长沙（望城） 103',
              label: '长沙（望城） 103'
            }, {
              value: '常德 102',
              label: '常德 102'
            }, {
              value: '吉首 101',
              label: '吉首 101'
            }, {
              value: '南县 100',
              label: '南县 100'
            }, {
              value: '石门 99',
              label: '石门 99'
            }]
          }, {
            value: '湖北',
            label: '湖北',
            children: [{
              value: '武汉 98',
              label: '武汉 98'
            }, {
              value: '宜昌 97',
              label: '宜昌 97'
            }, {
              value: '鄂西 96',
              label: '鄂西 96'
            }, {
              value: '麻城 95',
              label: '麻城 95'
            }, {
              value: '钟祥 94',
              label: '钟祥 94'
            }, {
              value: '老河口 93',
              label: '老河口 93'
            }, {
              value: '陨西 92',
              label: '陨西 92'
            }]
          }, {
            value: '河南',
            label: '河南',
            children: [{
              value: '尚丘 91',
              label: '尚丘 91'
            }, {
              value: '信阳 90',
              label: '信阳 90'
            }, {
              value: '驻马店 89',
              label: '驻马店 89'
            }, {
              value: '南阳 88',
              label: '南阳 88'
            }, {
              value: '郑州 87',
              label: '郑州 87'
            }, {
              value: '卢氏 86',
              label: '卢氏 86'
            }, {
              value: '安阳 85',
              label: '安阳 85'
            }]
          }]
        }, {
          value: '华北地区',
          label: '华北地区',
          children: [{
            value: '内蒙古',
            label: '内蒙古',
            children: [{
              value: '赤峰 84',
              label: '赤峰 84'
            }, {
              value: '多伦 83',
              label: '多伦 83'
            }, {
              value: '通辽 82',
              label: '通辽 82'
            }, {
              value: '开鲁 81',
              label: '开鲁 81'
            }, {
              value: '林西 80',
              label: '林西 80'
            }, {
              value: '锡林浩特 79',
              label: '锡林浩特 79'
            }, {
              value: '巴林左旗 78',
              label: '巴林左旗 78'
            }, {
              value: '扎鲁特旗 77',
              label: '扎鲁特旗 77'
            }, {
              value: '西乌珠穆沁旗 76',
              label: '西乌珠穆沁旗 76'
            }, {
              value: '东胜 75',
              label: '东胜 75'
            }, {
              value: '鄂托克旗 74',
              label: '鄂托克旗 74'
            }, {
              value: '古兰太 73',
              label: '古兰太 73'
            }, {
              value: '呼和浩特 72',
              label: '呼和浩特 72'
            }, {
              value: '化德 71',
              label: '化德 71'
            }, {
              value: '达尔汗联合旗 70',
              label: '达尔汗联合旗 70'
            }, {
              value: '乌特拉后旗 69',
              label: '乌特拉后旗 69'
            }, {
              value: '朱日和 68',
              label: '朱日和 68'
            }, {
              value: '海力索 67',
              label: '海力索 67'
            }, {
              value: '阿巴嘎旗 66',
              label: '阿巴嘎旗 66'
            }, {
              value: '二连浩特 65',
              label: '二连浩特 65'
            }, {
              value: '巴音毛道 64',
              label: '巴音毛道 64'
            }, {
              value: '额济纳旗 63',
              label: '额济纳旗 63'
            }, {
              value: '东乌珠穆沁旗 62',
              label: '东乌珠穆沁旗 62'
            }, {
              value: '索伦 61',
              label: '索伦 61'
            }, {
              value: '阿尔山 60',
              label: '阿尔山 60'
            }, {
              value: '博克图 59',
              label: '博克图 59'
            }, {
              value: '海拉尔 58',
              label: '海拉尔 58'
            }, {
              value: '满洲里 57',
              label: '满洲里 57'
            }, {
              value: '图里河 56',
              label: '图里河 56'
            }]
          }, {
            value: '山西',
            label: '山西',
            children: [{
              value: '侯马 55',
              label: '侯马 55'
            }, {
              value: '运城 54',
              label: '运城 54'
            }, {
              value: '介休 53',
              label: '介休 53'
            }, {
              value: '榆社 52',
              label: '榆社 52'
            }, {
              value: '太原 51',
              label: '太原 51'
            }, {
              value: '原平 50',
              label: '原平 50'
            }, {
              value: '大同 49',
              label: '大同 49'
            }]
          }, {
            value: '河北',
            label: '河北',
            children: [{
              value: '饶阳 48',
              label: '饶阳 48'
            }, {
              value: '乐亭 47',
              label: '乐亭 47'
            }, {
              value: '承德 46',
              label: '承德 46'
            }, {
              value: '怀来 45',
              label: '怀来 45'
            }, {
              value: '丰宁 44',
              label: '丰宁 44'
            }, {
              value: '邢台 43',
              label: '邢台 43'
            }, {
              value: '石家庄 42',
              label: '石家庄 42'
            }, {
              value: '张北 41',
              label: '张北 41'
            }]
          }, {
            value: '天津',
            label: '天津',
            children: [{
              value: '天津 40',
              label: '天津 40'
            }]
          }, {
            value: '北京',
            label: '北京',
            children: [{
              value: '北京 39',
              label: '北京 39'
            }, {
              value: '密云 38',
              label: '密云 38'
            }]
          }]
        }, {
          value: '东北地区',
          label: '东北地区',
          children: [{
            value: '辽宁',
            label: '辽宁',
            children: [{
              value: '大连 37',
              label: '大连 37'
            }, {
              value: '丹东 36',
              label: '丹东 36'
            }, {
              value: '宽甸 35',
              label: '宽甸 35'
            }, {
              value: '营口 34',
              label: '营口 34'
            }, {
              value: '兴城 33',
              label: '兴城 33'
            }, {
              value: '本溪 32',
              label: '本溪 32'
            }, {
              value: '沈阳 31',
              label: '沈阳 31'
            }, {
              value: '锦州 30',
              label: '锦州 30'
            }, {
              value: '新民 29',
              label: '新民 29'
            }, {
              value: '朝阳 28',
              label: '朝阳 28'
            }, {
              value: '彰武 27',
              label: '彰武 27'
            }]
          }, {
            value: '吉林',
            label: '吉林',
            children: [{
              value: '临江 26',
              label: '临江 26'
            }, {
              value: '延吉 25',
              label: '延吉 25'
            }, {
              value: '东港 24',
              label: '东港 24'
            }, {
              value: '敦化 23',
              label: '敦化 23'
            }, {
              value: '长春 22',
              label: '长春 22'
            }, {
              value: '四平 21',
              label: '四平 21'
            }, {
              value: '前鄂尔多斯 20',
              label: '前鄂尔多斯 20'
            }, {
              value: '自城 19',
              label: '自城 19'
            }]
          }, {
            value: '黑龙江',
            label: '黑龙江',
            children: [{
              value: '绥芬河 18',
              label: '绥芬河 18'
            }, {
              value: '牡丹江 17',
              label: '牡丹江 17'
            }, {
              value: '鸡西 16',
              label: '鸡西 16'
            }, {
              value: '尚志 15',
              label: '尚志 15'
            }, {
              value: '通河 14',
              label: '通河 14'
            }, {
              value: '哈尔滨 13',
              label: '哈尔滨 13'
            }, {
              value: '肇州 12',
              label: '肇州 12'
            }, {
              value: '佳木斯 11',
              label: '佳木斯 11'
            }, {
              value: '安达 10',
              label: '安达 10'
            }, {
              value: '富景 9',
              label: '富景 9'
            }, {
              value: '海伦 8',
              label: '海伦 8'
            }, {
              value: '齐齐哈尔 7',
              label: '齐齐哈尔 7'
            }, {
              value: '富裕 6',
              label: '富裕 6'
            }, {
              value: '克山 5',
              label: '克山 5'
            }, {
              value: '孙吴 4',
              label: '孙吴 4'
            }, {
              value: '嫩江 3',
              label: '嫩江 3'
            }, {
              value: '呼玛 2',
              label: '呼玛 2'
            }, {
              value: '漠河 1',
              label: '漠河 1'
            }]
          }]
        }]
      };
    }
  };
</script>


