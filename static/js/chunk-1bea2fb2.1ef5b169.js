(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1bea2fb2"],{"6b09":function(t,a,e){},"70db":function(t,a,e){"use strict";e.r(a);var n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"dustbin"},[e("el-col",{attrs:{span:4}},[e("work-space")],1),e("el-col",{attrs:{span:20}}),e("el-container",[e("el-main",[e("div",{staticStyle:{"margin-top":"20px"}},[e("span",{staticStyle:{width:"50%","font-size":"1.17em","font-weight":"bold"}},[t._v("回收站")]),e("span",{staticStyle:{float:"right"}},[e("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(a){t.chart=a},expression:"chart"}},[e("el-radio-button",{attrs:{label:"列表"}}),e("el-radio-button",{attrs:{label:"图标"}})],1)],1)]),e("div",{staticStyle:{"margin-top":"30px"}},["列表"===t.chart?e("doc-list",{attrs:{type:"dustbin"}}):e("doc-img",{attrs:{type:"dustbin"}})],1)]),e("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[e("div",[e("el-button",{attrs:{plain:"",type:"danger"}},[t._v("清空回收站")])],1),e("div",[e("el-button",{attrs:{plain:"",type:"warning"}},[t._v("全部恢复")])],1)])],1)],1)},i=[],r={name:"dustbin",data:function(){return{chart:""}},mounted:function(){this.init()},methods:{init:function(){localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标"},toNewDoc:function(){this.$router.push({name:"editorPage"})},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)}}},c=r,s=(e("ed01"),e("2877")),o=Object(s["a"])(c,n,i,!1,null,"333a2b90",null);a["default"]=o.exports},ed01:function(t,a,e){"use strict";var n=e("6b09"),i=e.n(n);i.a}}]);
//# sourceMappingURL=chunk-1bea2fb2.1ef5b169.js.map