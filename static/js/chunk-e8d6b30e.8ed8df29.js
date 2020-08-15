(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-e8d6b30e"],{"0767":function(e,t,i){"use strict";i.r(t);var n=function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{staticClass:"myTeams"},[i("el-col",{attrs:{span:4}},[i("work-space")],1),i("el-col",{attrs:{span:20}}),i("el-container",[i("el-main",[i("h3",[e._v("我的团队")]),i("el-row",{attrs:{gutter:20}},e._l(e.teams,(function(t,n){return i("el-col",{key:n,staticStyle:{"margin-bottom":"20px"},attrs:{span:4}},[i("div",{staticStyle:{"text-align":"center",height:"100px"}},[i("el-card",{staticClass:"teamCard",attrs:{shadow:"hover"},nativeOn:{mouseenter:function(t){e.isHover=!0},mouseleave:function(t){e.isHover=!1}}},[e.isHover?i("div",{staticStyle:{right:"5px","line-height":"5px",position:"absolute",top:"5px","font-size":"x-small"}},[i("el-tooltip",{attrs:{effect:"dark",placement:"bottom","hide-after":800,enterable:!1,content:"查看团队信息"}},[i("i",{staticClass:"el-icon-s-tools",on:{click:function(i){return e.handleClick(t.id)}}})])],1):e._e(),e.isHover?i("div",{staticStyle:{right:"5px","line-height":"5px",position:"absolute",top:"25px","font-size":"x-small"}},[i("el-tooltip",{attrs:{effect:"dark",placement:"bottom","hide-after":800,enterable:!1,content:"添加队员"}},[i("i",{staticClass:"el-icon-s-custom",on:{click:function(i){return e.addPeople(t.id)}}})])],1):e._e(),i("div",{staticStyle:{"font-size":"40px"}},[i("i",{staticClass:"el-icon-pie-chart",on:{click:function(i){return e.toOneTeam(t.id)}}})]),i("div",{staticStyle:{cursor:"pointer"},on:{click:function(i){return e.toOneTeam(t.id)}}},[e._v(e._s(t.name))])])],1)])})),1)],1),i("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[i("div",[i("el-button",{attrs:{plain:"",type:"primary"},on:{click:e.newTeam}},[e._v("创建团队")])],1),i("div",[i("el-button",{attrs:{plain:"",type:"primary"}},[e._v("管理全部团队")])],1)])],1),i("el-dialog",{attrs:{title:"团队详细信息",visible:e.infoDialog,width:"30%",center:""},on:{"update:visible":function(t){e.infoDialog=t}}},[i("div",{},[i("div",[i("span",{staticStyle:{width:"40px"}},[e._v("团队名：")]),e._v(e._s(e.Info.name))]),i("div",{staticStyle:{cursor:"pointer"}},[i("span",{staticStyle:{width:"40px"}},[e._v("创建者：")]),e._v(e._s(e.Info.builder))]),i("div",[i("span",{staticStyle:{width:"40px"}},[e._v("创建日期：")]),e._v(e._s(e.Info.create_time))]),i("el-divider"),i("div",[e._v("所有成员： "),e._l(e.Info.coworkers,(function(t,n){return i("div",{key:n,staticClass:"coworkers"},[i("el-avatar",{staticStyle:{cursor:"pointer","vertical-align":"sub"},attrs:{src:t.userImg,size:"small"}}),i("span",{staticStyle:{height:"28px","padding-right":"15px","margin-left":"10px"}},[e._v(e._s(t.userName))]),t.isBuilder?i("i",{staticClass:"el-icon-user"}):e._e(),t.isBuilder?e._e():i("el-link",{staticStyle:{position:"absolute",right:"15px",top:"10px"},attrs:{type:"danger"},on:{click:function(i){return e.checkMove(t)}}},[e._v(" 移除")])],1)}))],2),i("el-divider"),i("el-link",{staticStyle:{"font-size":"16px"},attrs:{plain:"",type:"primary"}},[e._v("分享")]),i("el-link",{staticStyle:{float:"right","font-size":"16px"},attrs:{plain:"",type:"danger"},on:{click:function(t){return e.Delete(e.Info.id)}}},[e._v("删除 ")])],1)]),i("folder-dialog",{attrs:{dialog:e.folderDialog,"doc-id":"","team-id":e.dialogTeam,type:e.type},on:{changeVisible:e.changeVisible}})],1)},a=[],o=(i("4160"),i("b0c0"),i("159b"),i("4ec3")),s=i("56d7"),l={name:"myTeam",data:function(){return{teams:[{id:1,name:"小学期1"},{id:2,name:"小学期2"}],folderDialog:!1,type:"",dialogTeam:"",Info:{id:1,builder:"Kelly",coworkers:[{userId:1,userName:"Kelly",isBuilder:!0,isCollected:!0,userImg:"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"},{userId:2,userName:"Kelly2",isBuilder:!1,isCollected:!0,userImg:"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"}]},infoDialog:!1,isHover:!1}},mounted:function(){this.init()},methods:{init:function(){var e=this;Object(o["g"])().then((function(t){200===t.status&&(e.teams=[],t.data.forEach((function(t){e.teams.push({id:t.id,name:t.name,create_time:Object(s["GetTime"])(t.create_time),builder:t.create_user.username})})))}))},toOneTeam:function(e){this.$router.push({name:"team",params:{teamId:e}})},changeVisible:function(e){this.folderDialog=e},newTeam:function(){this.type="newteam",this.folderDialog=!0},addPeople:function(e){this.type="teamwork",this.dialogTeam=e,this.folderDialog=!0},handleClick:function(e){var t=this;this.teams.forEach((function(i){i.id===e&&(t.Info=i)})),Object(o["c"])(this.Info.id).then((function(e){t.Info.coworkers=[],e.data.forEach((function(e,i){0===i&&(t.Info.builder=e.username),t.Info.coworkers.push({userId:e.id,userName:e.username,userImg:e.head,isBuilder:0===i}),console.log(e.id,t.Info.coworkers)}))})),this.infoDialog=!0},Delete:function(e){var t=this,i="确定要删除团队吗？";this.$confirm(i).then((function(i){console.log(e+i),t.infoDialog=!1}))},checkMove:function(e){var t=this,i="确定要移除ta吗？";this.$confirm(i).then((function(i){console.log(e+i),t.infoDialog=!1}))}}},r=l,c=(i("8064"),i("2877")),d=Object(c["a"])(r,n,a,!1,null,"93a5374c",null);t["default"]=d.exports},8064:function(e,t,i){"use strict";var n=i("e487"),a=i.n(n);a.a},e487:function(e,t,i){}}]);
//# sourceMappingURL=chunk-e8d6b30e.8ed8df29.js.map