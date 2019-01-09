<template>
  <el-tabs v-model="windsetting" type="card">
    <el-tab-pane label="选择风速风向" name="first">
      <wind-selector />
    </el-tab-pane>
    <el-tab-pane label="自定义风速风向" name="second">
      <wind-input />
    </el-tab-pane>
  </el-tabs>
</template>

<script>
  import WindSelector from './WindSelector.vue'
  import WindInput from './WindInput.vue'

  export default {
    data() {
      return {
        windsetting: 'first'
      };
    },
    components: {
      WindSelector,
      WindInput
    }
  };
</script>

<style scoped>
.el-tabs{
  width: 90%;
}
</style>
