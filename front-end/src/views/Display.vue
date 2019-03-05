<template>
  <div id="display">
    <router-view></router-view>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="50"
      @current-change='pageChange'>
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: 'display',
  methods: {
    pageChange: function(page){
      this.$router.push('/display/d' + page);
    }
  }
}
</script>

<style scoped>
.el-pagination {
  margin-top: 2%;
}
</style>
