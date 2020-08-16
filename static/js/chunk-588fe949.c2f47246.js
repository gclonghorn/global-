(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-588fe949"],{"0767":function(e,t,i){"use strict";i.r(t);var s=function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{staticClass:"myTeams"},[i("el-col",{attrs:{span:4}},[i("work-space")],1),i("el-col",{attrs:{span:20}}),i("el-container",[i("el-main",[i("h3",[e._v("我的团队")]),i("el-row",{attrs:{gutter:20}},e._l(e.teams,(function(t,s){return i("el-col",{key:s,staticStyle:{"margin-bottom":"20px"},attrs:{span:4}},[i("div",{staticStyle:{"text-align":"center",height:"100px"}},[i("el-card",{staticClass:"teamCard",attrs:{shadow:"hover"},nativeOn:{mouseenter:function(t){e.isHover=!0},mouseleave:function(t){e.isHover=!1}}},[e.isHover?i("div",{staticStyle:{right:"5px","line-height":"5px",position:"absolute",top:"5px","font-size":"x-small"}},[i("el-tooltip",{attrs:{effect:"dark",placement:"bottom","hide-after":800,enterable:!1,content:"查看团队信息"}},[i("i",{staticClass:"el-icon-s-tools",on:{click:function(i){return e.handleClick(t.id)}}})])],1):e._e(),e.isHover?i("div",{staticStyle:{right:"5px","line-height":"5px",position:"absolute",top:"25px","font-size":"x-small"}},[i("el-tooltip",{attrs:{effect:"dark",placement:"bottom","hide-after":800,enterable:!1,content:"添加队员"}},[i("i",{staticClass:"el-icon-s-custom",on:{click:function(i){return e.addPeople(t.id)}}})])],1):e._e(),i("div",{staticStyle:{"font-size":"40px"}},[i("i",{staticClass:"el-icon-pie-chart",on:{click:function(i){return e.toOneTeam(t.id)}}})]),i("div",{staticStyle:{cursor:"pointer"},on:{click:function(i){return e.toOneTeam(t.id)}}},[e._v(e._s(t.name))])])],1)])})),1)],1),i("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[i("div",[i("el-button",{attrs:{plain:"",type:"primary"},on:{click:e.newTeam}},[e._v("创建团队")])],1)])],1),i("el-dialog",{attrs:{title:"团队详细信息",visible:e.infoDialog,width:"30%",center:""},on:{"update:visible":function(t){e.infoDialog=t}}},[i("div",{},[i("div",[i("span",{staticStyle:{width:"40px"}},[e._v("团队名：")]),e._v(e._s(e.Info.name))]),i("div",{staticStyle:{cursor:"pointer"}},[i("span",{staticStyle:{width:"40px"}},[e._v("创建者：")]),e._v(e._s(e.Info.builder))]),i("div",[i("span",{staticStyle:{width:"40px"}},[e._v("创建日期：")]),e._v(e._s(e.Info.create_time))]),i("el-divider"),i("div",[e._v("所有成员： "),e._l(e.Info.coworkers,(function(t,s){return i("div",{key:s,staticClass:"coworkers"},[i("el-avatar",{staticStyle:{cursor:"pointer","vertical-align":"sub"},attrs:{src:t.userImg,size:"small"}}),i("span",{staticStyle:{height:"28px","padding-right":"15px","margin-left":"10px"}},[e._v(e._s(t.userName))]),t.isBuilder?i("i",{staticClass:"el-icon-user"}):e._e(),t.isBuilder?e._e():i("el-link",{staticStyle:{position:"absolute",right:"15px",top:"10px"},attrs:{type:"danger"},on:{click:function(i){return e.checkMove(t)}}},[e._v(" 移除")])],1)}))],2),i("el-divider"),i("el-link",{staticStyle:{float:"right","font-size":"16px"},attrs:{plain:"",type:"danger"},on:{click:function(t){return e.Delete(e.Info.id)}}},[e.userId===e.Info.builderId?i("span",[e._v("退出")]):i("span"),e._v("删除 ")])],1)]),i("folder-dialog",{attrs:{dialog:e.folderDialog,"doc-id":e.dialogTeam,type:e.type,name:e.NAME},on:{changeVisible:e.changeVisible}})],1)},n=[],a=(i("4160"),i("b0c0"),i("159b"),i("4ec3")),o=i("56d7"),r={name:"myTeam",data:function(){return{userId:localStorage.getItem("userId"),teams:[{id:1,name:"小学期1"},{id:2,name:"小学期2"}],folderDialog:!1,type:"",dialogTeam:"",Info:{id:1,builder:"Kelly",coworkers:[{userId:1,userName:"Kelly",isBuilder:!0,isCollected:!0,userImg:"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"},{userId:2,userName:"Kelly2",isBuilder:!1,isCollected:!0,userImg:"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"}]},infoDialog:!1,isHover:!1,NAME:""}},mounted:function(){this.init()},methods:{init:function(){var e=this;Object(a["q"])().then((function(t){200===t.status&&(e.teams=[],t.data.forEach((function(t){e.teams.push({id:t.id,name:t.name,create_time:Object(o["GetTime"])(t.create_time),builder:t.create_user.username,builderId:t.create_user.id})})))}))},toOneTeam:function(e){this.$router.push({name:"team",params:{teamId:e}})},changeVisible:function(e){this.folderDialog=e,this.init()},newTeam:function(){this.type="newteam",this.folderDialog=!0},addPeople:function(e){var t=this;this.type="teamwork",this.dialogTeam=e,this.teams.forEach((function(i){i.id+""!==e+""||(t.NAME=i.name)})),console.log(this.NAME),this.folderDialog=!0},handleClick:function(e){var t=this;this.teams.forEach((function(i){i.id===e&&(t.Info=i)})),Object(a["k"])(this.Info.id).then((function(e){t.Info.coworkers=[],console.log(e.data),e.data.forEach((function(e,i){0===i&&(t.Info.builder=e.username),t.Info.coworkers.push({userId:e.id,userName:e.username,userImg:e.head,isBuilder:0===i}),console.log(e.id,t.Info.coworkers)})),t.infoDialog=!0})).catch((function(e){t.$message({message:e.response.data,typd:"error"})}))},Delete:function(e){var t=this;if(this.userId===this.Info.builderId){var i="确定要退出团队吗？";this.$confirm(i).then((function(){Object(a["B"])(e,localStorage.getItem("userId")).then((function(e){200===e.status?t.$message({message:"退出团队成功",type:"warning"}):204==e.status&&t.$message({message:"发生其他错误，退出团队失败",type:"error"})})).catch((function(e){e.response&&401===e.response.status&&t.$message({message:"您没有删除权限或此人不在协作者中",type:"error"})}))}))}else{var s="确定要删除团队吗？";this.$confirm(s).then((function(){Object(a["e"])(e).then((function(e){204===e.status&&(t.$message({message:"删除团队成功",type:"info"}),t.init())})).catch((function(e){return t.$message({message:e.response.data,type:"error"})})),t.infoDialog=!1}))}},checkMove:function(e){var t=this,i="确定要移除ta吗？";this.$confirm(i).then((function(){Object(a["B"])(t.Info.id,e.userId).then((function(e){200===e.status?(t.Info.coworkers=[],e.data.forEach((function(e,i){0===i&&(t.Info.builder=e.username),t.Info.coworkers.push({userId:e.id,userName:e.username,userImg:e.head,isBuilder:0===i})})),t.$message({message:"移除成功",type:"info"})):t.$message({message:"发生其他错误",type:"error"})})).catch((function(e){401===e.response.status&&t.$message({message:"您没有删除权限或此人不在团队中",type:"error"})})),t.infoDialog=!1}))}}},c=r,l=(i("53fc"),i("2877")),u=Object(l["a"])(c,s,n,!1,null,"5c91a632",null);t["default"]=u.exports},"1dc3":function(e,t,i){},"53fc":function(e,t,i){"use strict";var s=i("1dc3"),n=i.n(s);n.a}}]);