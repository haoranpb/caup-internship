<template>
  <div id="display-3">
    <!-- 枝栽景观信息 -->
    <div class="img">
      <img src="@/assets/display-3.jpeg" width="40%" height="40%" alt="" />
    </div>
    <el-row>
      <el-col :span="12">
        <div class="imgcol">
          <p>夏天常绿树和落叶树</p>
          <img src="@/assets/3-a.png" alt="夏天常绿树和落叶树" />
        </div>
      </el-col>
      <el-col :span="12">
        <div class="imgcol">
          <p>冬天常绿</p>
          <img src="@/assets/3-b.png" alt="冬天常绿树" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'display-3',
}
</script>

<style scoped>
.img{
  width: 100%;
}
</style>
