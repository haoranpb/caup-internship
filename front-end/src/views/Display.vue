<template>
  <div id="display">
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
      console.log(page); // router.push()...
    }
  }
}
</script>