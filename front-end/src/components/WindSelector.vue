<template>
  <el-select v-model="value" placeholder="请选择风速条件">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</template>

<script>
  export default {
    data() {
      return {
        options: [{
          value: '选项1',
          label: '夏季'
        }, {
          value: '选项2',
          label: '冬季'
        }],
        value: ''
      }
    }
  }
</script>