<template>
  <div class="tree-management">
    <el-menu class="menu" :router=true>
      <el-menu-item index="1" route="tree-record">
        <span slot="title">树籍表</span>
      </el-menu-item>
      <el-menu-item index="2" route="tree-danger">
        <span slot="">危险度分集表</span>
      </el-menu-item>
      <el-menu-item index="3" route="tree-maintain">
        <span slot="title">维护管理记录</span>
      </el-menu-item>
    </el-menu>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios'
import { constants } from 'crypto';

export default {
  data() {
    return {

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
.menu{
  width: 15%;
  float: left;
}
</style>