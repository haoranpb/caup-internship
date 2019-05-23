<template>
  <div class="tree">
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="树木编号">
        <el-input v-model="form.code"></el-input>
      </el-form-item>
      <el-form-item label="（原树编号）">
        <el-input v-model="form.oldcode"></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="调查日">
        <el-date-picker v-model="form.date" type="date" placeholder="选择日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="气候">
        <el-input v-model="form.weather"></el-input>
      </el-form-item>
      <el-form-item label="调查人">
        <el-input v-model="form.people"></el-input>
      </el-form-item>
    </el-form>
    <el-form :inline="true" :model="form" label-width="100px">
      <el-form-item label="树种名">
        <el-input v-model="form.treetype"></el-input>
      </el-form-item>
      <el-form-item label="学名">
        <el-input v-model="form.scientificname"></el-input>
      </el-form-item>
      <el-form-item label="科名">
        <el-input v-model="form.arcypteridae"></el-input>
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
        code: '',
        oldcode: '',
        date: '',
        weather: '',
        people: '',
        treetype: '',
        scientificname: '',
        arcypteridae: ''
      }
    }
  },
  methods: {
    onSubmit() {
      let obj = this;
      var params = new URLSearchParams();
      params.append('formdata', obj.form);

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api',
        data: params,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
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
</style>