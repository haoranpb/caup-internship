<template>
  <div>
    <el-input
      placeholder="请输入风向"
      v-model="input1"
      clearable>
    </el-input>
    <el-input
      placeholder="请输入风速(m/s)"
      v-model="input2"
      clearable>
    </el-input>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        input1: '',
        input2: ''
      }
    }
  }
</script>

<style scoped>
.el-input{
  width: 60%;
}
</style>
