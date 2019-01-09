<template>
  <el-select
    v-model="value"
    placeholder="模型范围大小: X, Y, Z">
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
          label: 'X, Y, Z (<100m, <100m, <50m)'
        }, {
          value: '选项2',
          label: 'X, Y, Z (<250m, <250m, <100m)'
        }],
        value: ''
      }
    }
  }
</script>