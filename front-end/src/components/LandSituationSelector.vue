<template>
  <el-select v-model="value" placeholder="地况条件">
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
          label: '地况A：海岸、湖岸（建筑稀疏地区）'
        }, {
          value: '选项2',
          label: '地况B：乡镇和城市郊区'
        }, {
          value: '选项3',
          label: '地况C：密集建筑群的城市市区'
        }, {
          value: '选项4',
          label: '地况D：密集且房屋较高的城市市区'
        }],
        value: ''
      }
    }
  }
</script>