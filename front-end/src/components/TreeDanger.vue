<template>
  <div id="tree-danger">
    <el-form :inline="true" :model="getForm" class="get-form">
      <el-form-item label="ID">
        <el-input v-model="getForm.id" placeholder="ID"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="search">查询</el-button>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px" class="rightform">
      <el-form-item label="表单ID">
        <el-input v-model="form.id"></el-input>
      </el-form-item>
      <el-form-item label="诊断日期">
        <el-date-picker v-model="form.diagnoseDate" type="date" placeholder="选择日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="诊断人">
        <el-input v-model="form.diagnoser"></el-input>
      </el-form-item>
      <el-form-item label="前次诊断日期">
        <el-date-picker v-model="form.lastDiagDate" type="date" placeholder="选择日期"></el-date-picker>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px" class="rightform">
      <el-form-item label="树种名">
        <el-input v-model="form.treeSpecies"></el-input>
      </el-form-item>
      <el-form-item label="数目编号">
        <el-input v-model="form.treeNumber"></el-input>
      </el-form-item>
    </el-form>
    <div class="divide">
      <p>植株外观基础判断</p>
    </div>
    <el-form class="rightform" :model="form" label-width="100px">
      <el-form-item label="活力度">
        <el-radio-group v-model="form.vigour">
          <el-radio :label=1>A 健全</el-radio>
          <el-radio :label=2>B 大致良好</el-radio>
          <el-radio :label=3>C 有异常</el-radio>
          <el-radio :label=4>D 衰退中</el-radio>
          <el-radio :label=5>E 不健全</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="粗枝及副杆">
        <el-radio-group v-model="form.thickstem">
          <el-radio :label=1>A 健全</el-radio>
          <el-radio :label=2>B 大致良好</el-radio>
          <el-radio :label=3>C 有受害</el-radio>
          <el-radio :label=4>D 受害多</el-radio>
          <el-radio :label=5>E 需要切除，但切除后树干变形</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="枝杆">
        <el-radio-group v-model="form.stems">
          <el-radio :label=1>A 健全</el-radio>
          <el-radio :label=2>B 大致良好</el-radio>
          <el-radio :label=3>C 有受害</el-radio>
          <el-radio :label=4>D 受害多</el-radio>
          <el-radio :label=5>E 损害具有危险性</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="树干分歧部">
        <el-radio-group v-model="form.branches">
          <el-radio :label=1>A 健全</el-radio>
          <el-radio :label=2>B 大致良好</el-radio>
          <el-radio :label=3>C 有受害</el-radio>
          <el-radio :label=4>D 受害多</el-radio>
          <el-radio :label=5>E 损害具有危险性</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="树干基部">
        <el-radio-group v-model="form.base">
          <el-radio :label=1>A 健全</el-radio>
          <el-radio :label=2>B 大致良好</el-radio>
          <el-radio :label=3>C 有受害</el-radio>
          <el-radio :label=4>D 受害多</el-radio>
          <el-radio :label=5>E 损害具有危险性</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="精密诊断必要">
        <el-radio-group v-model="form.diagNeccessity">
          <el-radio :label=1>A 不必要</el-radio>
          <el-radio :label=2>B 必要</el-radio>
        </el-radio-group>
      </el-form-item>
    </el-form>
    <div class="rightform">
      <div class="leftlabel">
        <p>附注</p>
      </div>
      <el-form :model="form" label-width="100px">
        <el-form-item label="1.空洞">
          <el-radio-group v-model="form.holePosition">
            <el-radio :label=1>A 有空洞</el-radio>
            <el-radio :label=2>B 无空洞</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="3.其他">
          <el-input type="textarea" v-model="form.noteOthers"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <div class="divide">
      <p>危险度分级</p>
    </div>
    <el-form class="rightform" :model="form" label-width="110px">
      <el-form-item label="连根拔起">
        <el-radio-group v-model="form.uprooted">
          <el-radio :label=1>0 安全</el-radio>
          <el-radio :label=2>1 轻微</el-radio>
          <el-radio :label=3>2 中等</el-radio>
          <el-radio :label=4>3 有危险</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="树干折损">
        <el-radio-group v-model="form.wreck">
          <el-radio :label=1>0 安全</el-radio>
          <el-radio :label=2>1 轻微</el-radio>
          <el-radio :label=3>2 中等</el-radio>
          <el-radio :label=4>3 有危险</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="粗杆折损">
        <el-radio-group v-model="form.thickstemWreck">
          <el-radio :label=1>0 安全</el-radio>
          <el-radio :label=2>1 轻微</el-radio>
          <el-radio :label=3>2 中等</el-radio>
          <el-radio :label=4>3 有危险</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="中小枝掉落">
        <el-radio-group v-model="form.branchFall">
          <el-radio :label=1>0 安全</el-radio>
          <el-radio :label=2>1 轻微</el-radio>
          <el-radio :label=3>2 中等</el-radio>
          <el-radio :label=4>3 有危险</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="树干倾斜及方向">
        <el-radio-group v-model="form.tilt">
          <el-radio :label=1>0 安全</el-radio>
          <el-radio :label=2>1 轻微</el-radio>
          <el-radio :label=3>2 中等</el-radio>
          <el-radio :label=4>3 有危险</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="其他">
        <el-input type="textarea" v-model="form.riskOthers"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return{
      getForm: {
        id: 1
      },
      form: {
        diagnoseDate: '2019-07-01T11:23:57.934Z',
        lastDiagDate: '2019-07-01T11:23:57.934Z',
        diagnoser: '',
        treeNumber: 0,
        treeSpecies: '',
        vigour: 0,
        thickstem: 0,
        stems: 0,
        base: 0,
        branches: 0,
        diagNeccessity: 0,
        holePosition: 0,
        noteOthers: '',
        uprooted: 0,
        wreck: 0,
        thickstemWreck: 0,
        tilt: 0,
        branchFall: 0,
        riskOthers: '',

        dangerRankcol: '',
        diagHeight: 0,
        id: 0,
        note: 0,
        trimTraceQuantity: 0,
        trimTraceSize: 0,
      }
    }
  },
  methods: {
    onSubmit() {
      let self = this;

      axios({
        method: 'post',
        url: 'http://47.100.50.80:8077/saveDangerRecord',
        data: self.form,
        headers: { 'Content-Type': 'application/json' }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function () {
        self.$message.error('糟糕，哪里出了点问题！');
      });
    },
    search(){
      let self = this;

      axios({
        method: 'post',
        url: 'http://47.100.50.80:8077/getDangerRecord',
        data: self.getForm.id,
        headers: { 'Content-Type': 'application/json' }
      })
      .then(function (response) {
        console.log(response);
        self.form = response.data;
      })
      .catch(function () {
        self.$message.error('糟糕，哪里出了点问题！');
      });
    }
  }
}
</script>

<style scoped>
.divide{
  height: 50px;
  width: 80%;
  margin-top: 30px;
  margin-bottom: 30px;
  float: right;
  font-size: 1.1em;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.rightform{
  float: right;
  width: 70%;
  margin-right: 9%;
}
.leftlabel{
  float: left;
  text-align: center;
  width: 10%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.get-form{
  text-align: center;
}
</style>
