(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0fd178a1"],{1399:function(t,a,e){"use strict";e.r(a);var n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"collection"},[e("el-col",{attrs:{span:4}},[e("work-space")],1),e("el-col",{attrs:{span:20}}),e("el-container",[e("el-main",[e("div",{staticStyle:{"margin-top":"20px"}},[e("span",{staticStyle:{width:"50%","font-size":"1.17em","font-weight":"bold"}},[t._v("我的收藏夹")]),e("span",{staticStyle:{float:"right"}},[e("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(a){t.chart=a},expression:"chart"}},[e("el-radio-button",{attrs:{label:"列表"}}),e("el-radio-button",{attrs:{label:"图标"}})],1)],1)]),e("div",{staticStyle:{"margin-top":"30px"}},["列表"===t.chart?e("doc-list",{attrs:{type:"collection"}}):e("doc-img",{attrs:{type:"collection"}})],1)]),e("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[e("div",[e("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toNewDoc}},[t._v("新建文档")])],1),e("div",[e("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toTemplate}},[t._v("模板库")])],1)])],1)],1)},i=[],c={name:"collection",data:function(){return{chart:""}},mounted:function(){this.init()},methods:{init:function(){localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标"},toNewDoc:function(){this.$router.push({name:"editorPage"})},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)},toTemplate:function(){this.$router.push({name:"templates"})}}},o=c,l=(e("3b35"),e("2877")),r=Object(l["a"])(o,n,i,!1,null,"1cb47e23",null);a["default"]=r.exports},"3b35":function(t,a,e){"use strict";var n=e("9a36"),i=e.n(n);i.a},"9a36":function(t,a,e){}}]);
//# sourceMappingURL=chunk-0fd178a1.2f950d1b.js.map