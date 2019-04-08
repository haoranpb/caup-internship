<template>
  <div id="display-4">
    <el-row>
      <el-col :span="12">
        <div>
          <p>夏天日照分布</p>
          <img class="img" src="@/assets/4-a.png" alt="夏天日照分布" />
        </div>
      </el-col>
      <el-col :span="12">
        <div>
          <p>夏天风速分布</p>
          <img class="img" src="@/assets/4-b.png" alt="夏天风速分布" />
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12">
        <div>
          <p>冬天日照分布</p>
          <img class="img" src="@/assets/4-c.png" alt="冬天日照分布" />
        </div>
      </el-col>
      <el-col :span="12">
        <div>
          <p>冬天风速分布</p>
          <img class="img" src="@/assets/4-d.png" alt="冬天风速分布" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'display-4',
}
</script>

<style scoped>
.img{
  width: 80%;
  height: 80%;
}
</style>
