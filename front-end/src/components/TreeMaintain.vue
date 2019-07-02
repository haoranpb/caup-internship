<template>
  <div id="tree-maintain">
    <el-form :inline="true" :model="form" label-width="100px" class="rightform">
      <el-form-item label="管理日期">
        <el-date-picker v-model="form.date" type="date" placeholder="选择日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="前次诊断日期">
        <el-date-picker v-model="form.lastDate" type="date" placeholder="选择日期"></el-date-picker>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px" class="rightform">
      <el-form-item label="树木编号">
        <el-input v-model="form.treeNum"></el-input>
      </el-form-item>
      <el-form-item label="记录者">
        <el-input v-model="form.recorder"></el-input>
      </el-form-item>
      <el-form-item label="天气">
        <el-input v-model="form.climate"></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="施做项目">
        <el-radio-group v-model="form.project">
          <el-radio :label=1>A 修剪</el-radio>
          <el-radio :label=2>B 腐朽及衰退处理</el-radio>
          <el-radio :label=3>C 移除樱花树干部与枝条之附属物</el-radio>
          <el-radio :label=4>D 施肥</el-radio>
          <el-radio :label=5>E 其他</el-radio>
        </el-radio-group>
      </el-form-item>
    </el-form>
    <div class="beforeImage">
      <h2>施做前（照片）</h2>
      <el-upload
        :auto-upload="false"
        list-type="picture-card"
        :on-preview="handleBeforePreview">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog :visible.sync="beforeVisible">
        <img width="100%" :src="beforeImage" alt="">
      </el-dialog>
    </div>
    <div class="afterImage">
      <h2>施做后（照片）</h2>
      <el-upload
        :auto-upload="false"
        list-type="picture-card"
        :on-preview="handleAfterPreview">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog :visible.sync="afterVisible">
        <img width="100%" :src="afterImage" alt="">
      </el-dialog>
    </div>
    <el-form :model="form" label-width="100px" class="rightform note">
      <el-form-item label="附注">
        <el-input type="textarea" v-model="form.note"></el-input>
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
      form: {
        date: '2019-07-01T11:23:57.944Z',
        lastDate: '2019-07-01T11:23:57.944Z',
        treeNum: 0,
        recorder: '',
        climate: '',
        project: 0,
        note: '',

        id: 0,
        photoBefore: '',
        photoAfter: '',

      },
      beforeImage: '',
      beforeVisible: false,
      afterImage: '',
      afterVisible: false
    }
  },
  methods: {
    handleBeforePreview(file) {
      this.beforeImage = file.url;
      this.beforeVisible = true;
    },
    handleAfterPreview(file){
      this.afterImage = file.url;
      this.afterVisible = true;
    },
    onSubmit() {
      let self = this;

      axios({
        method: 'post',
        url: 'http://47.100.50.80:8077/saveMaintainRecord',
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
.rightform{
  float: right;
  width: 70%;
  margin-right: 9%;
}
h2{
  font-size: 1.2em;
}
.note{
  margin-top: 2%;
}
</style>

