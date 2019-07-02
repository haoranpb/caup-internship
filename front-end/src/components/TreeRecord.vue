<template>
  <div class="tree">
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="树木编号">
        <el-input v-model="form.number"></el-input>
      </el-form-item>
      <el-form-item label="（原树编号）">
        <el-input v-model="form.oldNum"></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="调查日">
        <el-date-picker v-model="form.recordDate" type="date" placeholder="选择日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="气候">
        <el-input v-model="form.climate"></el-input>
      </el-form-item>
      <el-form-item label="调查人">
        <el-input v-model="form.investigator"></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="树种名">
        <el-input v-model="form.treeSpecies"></el-input>
      </el-form-item>
      <el-form-item label="学名">
        <el-input v-model="form.treeScientificName"></el-input>
      </el-form-item>
      <!-- <el-form-item label="科名"> 没在 API 找到对应的项
        <el-input v-model="form.arcypteridae"></el-input>
      </el-form-item> -->
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="位置">
        <el-input v-model="form.position"></el-input>
      </el-form-item>
      <el-form-item label="所有者">
        <el-input v-model="form.owner"></el-input>
      </el-form-item>
    </el-form>
    <el-form :model="form" label-width="100px">
      <el-form-item label="对象树木状况">
        <el-radio-group v-model="form.condition">
          <el-radio :label=1>单植</el-radio>
          <el-radio :label=2>列植</el-radio>
          <el-radio :label=3>群植</el-radio>
        </el-radio-group>
      </el-form-item>
    </el-form>
    <div style="height:200px">
      <div class="leftlabel">
        <p>气候</p>
      </div>
      <el-form :inline="true" :model="form" label-width="100px">
        <el-form-item label="年平均气温">
          <el-input v-model="form.avgTemperature" placeholder="℃"></el-input>
        </el-form-item>
        <el-form-item label="最高气温">
          <el-input v-model="form.heigTemperature" placeholder="℃"></el-input>
        </el-form-item>
        <el-form-item label="最低气温">
          <el-input v-model="form.lowTemperature" placeholder="℃"></el-input>
        </el-form-item>
      </el-form>
      <el-form :inline="true" :model="form" label-width="100px">
        <el-form-item label="年降水量">
          <el-input v-model="form.annualPrecipitation" placeholder="mm"></el-input>
        </el-form-item>
        <el-form-item label="风环境">
          <el-input v-model="form.windSpeed" placeholder="公尺/秒"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <div style="height:500px">
      <div class="leftlabel">
        <p>生长环境</p>
      </div>
      <el-form class="rightform" :model="form" label-width="100px">
        <el-form-item label="立地场所">
          <el-input v-model="form.place"></el-input>
        </el-form-item>
        <el-form-item label="周围状况">
          <el-radio-group v-model="form.surroundCondition">
            <el-radio :label=1>1.树木（a.大面积</el-radio>
            <el-radio :label=2>b.小面积）</el-radio>
            <el-radio :label=3>2.草地</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="日照不足原因">
          <el-input v-model="form.sunlightReason"></el-input>
        </el-form-item>
        <el-form-item label="土壤">
          <el-radio-group v-model="form.soil">
            <el-radio :label=1>1.自然土a.堆土</el-radio>
            <el-radio :label=2>b.崩土</el-radio>
            <el-radio :label=3>2.填土客土</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="地形">
          <el-radio-group v-model="form.terrain">
            <el-radio :label=1>1.山地</el-radio>
            <el-radio :label=2>2.丘陵地</el-radio>
            <el-radio :label=3>3.台地</el-radio>
            <el-radio :label=4>4.低湿地</el-radio>
            <el-radio :label=5>5.山腰</el-radio>
            <el-radio :label=6>6.山谷</el-radio>
            <el-radio :label=7>7.洼地</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="树干基部">
          <el-radio-group v-model="form.surroundHerb">
            <el-radio :label=1>1.密生</el-radio>
            <el-radio :label=2>2.散生</el-radio>
            <el-radio :label=3>3.无</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="周围植生">
          <el-radio-group v-model="form.surroundWoody">
            <el-radio :label=1>1.密生</el-radio>
            <el-radio :label=2>2.散生</el-radio>
            <el-radio :label=3>3.无</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="周围树木关系">
          <el-radio-group v-model="form.surroundRelation">
            <el-radio :label=1>1.无影响</el-radio>
            <el-radio :label=2>2.稍微影响</el-radio>
            <el-radio :label=3>3.有影响</el-radio>
            <el-radio :label=4>4.相当受影响</el-radio>
            <el-radio :label=5>5.非常受影响</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-form>
    </div>
    <div style="height:200px">
      <div class="leftlabel">
        <p>管理状况</p>
      </div>
      <el-form class="rightform" :model="form" label-width="100px">
      <!-- <el-form-item label="1.栏杆">
        <el-radio-group v-model="form.pillar">
          <el-radio :label=1>A.有：a.高度（cm）</el-radio>
          <el-radio :label=2>b.材质</el-radio>
          <el-radio :label=3>群植</el-radio>
        </el-radio-group>
      </el-form-item> -->
      <el-form-item label="2.支柱">
        <el-radio-group v-model="form.pillar">
          <el-radio :label=1>A.有：a.良好</el-radio>
          <el-radio :label=2>b.不良</el-radio>
          <el-radio :label=3>c.受损</el-radio>
          <el-radio :label=4>B.无</el-radio>
        </el-radio-group>
      </el-form-item>
            <el-form-item label="3.修剪">
        <el-radio-group v-model="form.trim">
          <el-radio :label=1>A.强</el-radio>
          <el-radio :label=2>B.弱</el-radio>
          <el-radio :label=3>C.无</el-radio>
        </el-radio-group>
      </el-form-item>
      <!-- <el-form-item label="4.施肥">
        <el-radio-group v-model="form.pillar">
          <el-radio :label=1>A.有：a.高度（cm）</el-radio>
          <el-radio :label=2>b.材质</el-radio>
          <el-radio :label=3>群植</el-radio>
        </el-radio-group>
      </el-form-item> -->
      </el-form>
    </div>
    <div style="height:200px">
      <div class="leftlabel">
        <p>形状大小</p>
      </div>
      <el-form :inline="true" :model="form" label-width="100px">
        <el-form-item label="树高">
          <el-input v-model="form.treeHeight" placeholder="m"></el-input>
        </el-form-item>
        <el-form-item label="主干胸高（1.3m周围）">
          <el-input v-model="form.treeGirth" placeholder="cm"></el-input>
        </el-form-item>
        <el-form-item label="树龄">
          <el-input v-model="form.treeAge" placeholder="年"></el-input>
        </el-form-item>
        <el-form-item label="树皮状况">
          <el-input v-model="form.treeBark"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <el-form :model="form" label-width="100px">
      <el-form-item label="树干基部状况">
        <el-radio-group v-model="form.treeBaseCondition">
          <el-radio :label=1>1.不毛之地</el-radio>
          <el-radio :label=2>2.草地：地被类</el-radio>
          <el-radio :label=3>3.灌木</el-radio>
          <el-radio :label=4>4.铺装</el-radio>
          <el-radio :label=5>5.覆土厚度（）土性（）</el-radio>
          <el-radio :label=6>6.其他（）</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="特别记载">
        <el-input type="textarea" v-model="form.records"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'
import { constants } from 'crypto';

export default {
  data() {
    return {
      form: {
        number: 0,
        oldNum: 0,
        recordDate: '2019-07-01T11:23:57.951Z',
        climate: '',
        investigator: '',
        treeSpecies: '',
        treeScientificName: '',
        position: '',
        owner: '',
        condition: 0,
        avgTemperature: 0,
        heigTemperature: 0,
        lowTemperature: 0,
        annualPrecipitation: 0,
        windSpeed: 0,
        place: '',
        sunlightReason: '',
        surroundCondition: 0,
        terrain: 0,
        soil: 0,
        surroundHerb: 0,
        surroundWoody: 0,
        surroundRelation: 0,
        pillar: 0,
        trim: 0,
        treeHeight: 0,
        treeAge: 0,
        treeBark: '',
        treeGirth: 0,
        treeBaseCondition: 0,
        records: '',

        area: 0,
        fertiTpy: 0,
        fertiType: 0,
        fertilization: 0,
        handrail: 0,
        handrailArea: 0,
        handrailHeight: 0,
        handrailMaterial: '',
        handrailYear: 0,
        id: 0,
        others: '',
        scArea: 0,
        soilThickness: 0,
        soilType: '',
        year: 0
      }
    }
  },
  methods: {
    onSubmit() {
      let self = this;

      axios({
        method: 'post',
        url: 'http://47.100.50.80:8077/saveTreeRecord',
        data: self.form,
        headers: { 'Content-Type': 'application/json' }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function () {
        self.$message.error('糟糕，哪里出了点问题！');
      });
    }
  }
}
</script>

<style scoped>
.tree{
  margin-left: 20%;
  margin-right: 20%;
  width: 60%;
  text-align: left;
}
.leftlabel{
  float: left;
  text-align: center;
  width: 10%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.rightform{
  float: right;
  width: 80%;
  margin-right: 9%;
}
</style>