// import request from '../utils/request'
//
// // 查询
// export function fetchList(data) {
//   return request.post('/activity/page', data, {
//     trim: true
//   })
// }
//
// export function fetchActivityList(data) {
//   return request.post('/activity/page', data, {
//     trim: true
//   })
// }
//
// // 创建
// export function create(data) {
//   return request.post('/activity/create', data)
// }
//
// // 修改
// export function updateById(data) {
//   return request.post('/activity/updateById', data)
// }
//
// export function cancel(data) {
//   return request.post('/activity/cancel', data)
// }
//
// export function check(data) {
//   return request.post('/activity/check', data)
// }
//
//
// // 分数回滚
// export function reScore(data) {
//   return request.post('/activity/reScore', data)
// }
//
// // 删除
// export function deleteById(id) {
//   return request.get(`/activity/delete/${id}`)
// }
//
// // 获取详情
// export function findActivityById(data) {
//   return request.get(`/activity/findOne`,{
//     params: data
//   })
// }
//
// // 批量删除
// export function deleteByIdInBatch(ids) {
//   return request.get(`/activity/delete/batch`, {
//     params: {
//       ids
//     }
//   })
// }
//
