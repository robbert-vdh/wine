# Automatically generated from Vulkan vk.xml; DO NOT EDIT!
#
# This file is generated from Vulkan vk.xml file covered
# by the following copyright and permission notice:
#
# Copyright (c) 2015-2018 The Khronos Group Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ---- Exceptions to the Apache 2.0 License: ----
#
# As an exception, if you use this Software to generate code and portions of
# this Software are embedded into the generated code as a result, you may
# redistribute such product without providing attribution as would otherwise
# be required by Sections 4(a), 4(b) and 4(d) of the License.
#
# In addition, if you combine or link code generated by this Software with
# software that is licensed under the GPLv2 or the LGPL v2.0 or 2.1
# ("`Combined Software`") and if a court of competent jurisdiction determines
# that the patent provision (Section 3), the indemnity provision (Section 9)
# or other Section of the License conflicts with the conditions of the
# applicable GPL or LGPL license, you may retroactively and prospectively
# choose to deem waived or otherwise exclude such Section(s) of the License,
# but only in their entirety and only with respect to the Combined Software.
#

@ stdcall vk_icdGetInstanceProcAddr(ptr str) wine_vk_icdGetInstanceProcAddr
@ stdcall vk_icdNegotiateLoaderICDInterfaceVersion(ptr) wine_vk_icdNegotiateLoaderICDInterfaceVersion
@ stub vkAcquireNextImage2KHR
@ stdcall wine_vkAcquireNextImageKHR(ptr int64 int64 int64 int64 ptr)
@ stdcall wine_vkAllocateCommandBuffers(ptr ptr ptr)
@ stdcall wine_vkAllocateDescriptorSets(ptr ptr ptr)
@ stdcall wine_vkAllocateMemory(ptr ptr ptr ptr)
@ stdcall wine_vkBeginCommandBuffer(ptr ptr)
@ stdcall wine_vkBindBufferMemory(ptr int64 int64 int64)
@ stdcall wine_vkBindBufferMemory2(ptr long ptr)
@ stdcall wine_vkBindImageMemory(ptr int64 int64 int64)
@ stdcall wine_vkBindImageMemory2(ptr long ptr)
@ stdcall wine_vkCmdBeginQuery(ptr int64 long long)
@ stdcall wine_vkCmdBeginRenderPass(ptr ptr long)
@ stdcall wine_vkCmdBindDescriptorSets(ptr long int64 long long ptr long ptr)
@ stdcall wine_vkCmdBindIndexBuffer(ptr int64 int64 long)
@ stdcall wine_vkCmdBindPipeline(ptr long int64)
@ stdcall wine_vkCmdBindVertexBuffers(ptr long long ptr ptr)
@ stdcall wine_vkCmdBlitImage(ptr int64 long int64 long long ptr long)
@ stdcall wine_vkCmdClearAttachments(ptr long ptr long ptr)
@ stdcall wine_vkCmdClearColorImage(ptr int64 long ptr long ptr)
@ stdcall wine_vkCmdClearDepthStencilImage(ptr int64 long ptr long ptr)
@ stdcall wine_vkCmdCopyBuffer(ptr int64 int64 long ptr)
@ stdcall wine_vkCmdCopyBufferToImage(ptr int64 int64 long long ptr)
@ stdcall wine_vkCmdCopyImage(ptr int64 long int64 long long ptr)
@ stdcall wine_vkCmdCopyImageToBuffer(ptr int64 long int64 long ptr)
@ stdcall wine_vkCmdCopyQueryPoolResults(ptr int64 long long int64 int64 int64 long)
@ stdcall wine_vkCmdDispatch(ptr long long long)
@ stub vkCmdDispatchBase
@ stdcall wine_vkCmdDispatchIndirect(ptr int64 int64)
@ stdcall wine_vkCmdDraw(ptr long long long long)
@ stdcall wine_vkCmdDrawIndexed(ptr long long long long long)
@ stdcall wine_vkCmdDrawIndexedIndirect(ptr int64 int64 long long)
@ stdcall wine_vkCmdDrawIndirect(ptr int64 int64 long long)
@ stdcall wine_vkCmdEndQuery(ptr int64 long)
@ stdcall wine_vkCmdEndRenderPass(ptr)
@ stdcall wine_vkCmdExecuteCommands(ptr long ptr)
@ stdcall wine_vkCmdFillBuffer(ptr int64 int64 int64 long)
@ stdcall wine_vkCmdNextSubpass(ptr long)
@ stdcall wine_vkCmdPipelineBarrier(ptr long long long long ptr long ptr long ptr)
@ stdcall wine_vkCmdPushConstants(ptr int64 long long long ptr)
@ stdcall wine_vkCmdResetEvent(ptr int64 long)
@ stdcall wine_vkCmdResetQueryPool(ptr int64 long long)
@ stdcall wine_vkCmdResolveImage(ptr int64 long int64 long long ptr)
@ stdcall wine_vkCmdSetBlendConstants(ptr ptr)
@ stdcall wine_vkCmdSetDepthBias(ptr float float float)
@ stdcall wine_vkCmdSetDepthBounds(ptr float float)
@ stub vkCmdSetDeviceMask
@ stdcall wine_vkCmdSetEvent(ptr int64 long)
@ stdcall wine_vkCmdSetLineWidth(ptr float)
@ stdcall wine_vkCmdSetScissor(ptr long long ptr)
@ stdcall wine_vkCmdSetStencilCompareMask(ptr long long)
@ stdcall wine_vkCmdSetStencilReference(ptr long long)
@ stdcall wine_vkCmdSetStencilWriteMask(ptr long long)
@ stdcall wine_vkCmdSetViewport(ptr long long ptr)
@ stdcall wine_vkCmdUpdateBuffer(ptr int64 int64 int64 ptr)
@ stdcall wine_vkCmdWaitEvents(ptr long ptr long long long ptr long ptr long ptr)
@ stdcall wine_vkCmdWriteTimestamp(ptr long int64 long)
@ stdcall wine_vkCreateBuffer(ptr ptr ptr ptr)
@ stdcall wine_vkCreateBufferView(ptr ptr ptr ptr)
@ stdcall wine_vkCreateCommandPool(ptr ptr ptr ptr)
@ stdcall wine_vkCreateComputePipelines(ptr int64 long ptr ptr ptr)
@ stdcall wine_vkCreateDescriptorPool(ptr ptr ptr ptr)
@ stdcall wine_vkCreateDescriptorSetLayout(ptr ptr ptr ptr)
@ stdcall wine_vkCreateDescriptorUpdateTemplate(ptr ptr ptr ptr)
@ stdcall wine_vkCreateDevice(ptr ptr ptr ptr)
@ stub vkCreateDisplayModeKHR
@ stub vkCreateDisplayPlaneSurfaceKHR
@ stdcall wine_vkCreateEvent(ptr ptr ptr ptr)
@ stdcall wine_vkCreateFence(ptr ptr ptr ptr)
@ stdcall wine_vkCreateFramebuffer(ptr ptr ptr ptr)
@ stdcall wine_vkCreateGraphicsPipelines(ptr int64 long ptr ptr ptr)
@ stdcall wine_vkCreateImage(ptr ptr ptr ptr)
@ stdcall wine_vkCreateImageView(ptr ptr ptr ptr)
@ stdcall wine_vkCreateInstance(ptr ptr ptr)
@ stdcall wine_vkCreatePipelineCache(ptr ptr ptr ptr)
@ stdcall wine_vkCreatePipelineLayout(ptr ptr ptr ptr)
@ stdcall wine_vkCreateQueryPool(ptr ptr ptr ptr)
@ stdcall wine_vkCreateRenderPass(ptr ptr ptr ptr)
@ stdcall wine_vkCreateSampler(ptr ptr ptr ptr)
@ stdcall wine_vkCreateSamplerYcbcrConversion(ptr ptr ptr ptr)
@ stdcall wine_vkCreateSemaphore(ptr ptr ptr ptr)
@ stdcall wine_vkCreateShaderModule(ptr ptr ptr ptr)
@ stub vkCreateSharedSwapchainsKHR
@ stdcall wine_vkCreateSwapchainKHR(ptr ptr ptr ptr)
@ stdcall wine_vkCreateWin32SurfaceKHR(ptr ptr ptr ptr)
@ stdcall wine_vkDestroyBuffer(ptr int64 ptr)
@ stdcall wine_vkDestroyBufferView(ptr int64 ptr)
@ stdcall wine_vkDestroyCommandPool(ptr int64 ptr)
@ stdcall wine_vkDestroyDescriptorPool(ptr int64 ptr)
@ stdcall wine_vkDestroyDescriptorSetLayout(ptr int64 ptr)
@ stdcall wine_vkDestroyDescriptorUpdateTemplate(ptr int64 ptr)
@ stdcall wine_vkDestroyDevice(ptr ptr)
@ stdcall wine_vkDestroyEvent(ptr int64 ptr)
@ stdcall wine_vkDestroyFence(ptr int64 ptr)
@ stdcall wine_vkDestroyFramebuffer(ptr int64 ptr)
@ stdcall wine_vkDestroyImage(ptr int64 ptr)
@ stdcall wine_vkDestroyImageView(ptr int64 ptr)
@ stdcall wine_vkDestroyInstance(ptr ptr)
@ stdcall wine_vkDestroyPipeline(ptr int64 ptr)
@ stdcall wine_vkDestroyPipelineCache(ptr int64 ptr)
@ stdcall wine_vkDestroyPipelineLayout(ptr int64 ptr)
@ stdcall wine_vkDestroyQueryPool(ptr int64 ptr)
@ stdcall wine_vkDestroyRenderPass(ptr int64 ptr)
@ stdcall wine_vkDestroySampler(ptr int64 ptr)
@ stdcall wine_vkDestroySamplerYcbcrConversion(ptr int64 ptr)
@ stdcall wine_vkDestroySemaphore(ptr int64 ptr)
@ stdcall wine_vkDestroyShaderModule(ptr int64 ptr)
@ stdcall wine_vkDestroySurfaceKHR(ptr int64 ptr)
@ stdcall wine_vkDestroySwapchainKHR(ptr int64 ptr)
@ stdcall wine_vkDeviceWaitIdle(ptr)
@ stdcall wine_vkEndCommandBuffer(ptr)
@ stdcall wine_vkEnumerateDeviceExtensionProperties(ptr str ptr ptr)
@ stdcall wine_vkEnumerateDeviceLayerProperties(ptr ptr ptr)
@ stdcall wine_vkEnumerateInstanceExtensionProperties(str ptr ptr)
@ stub vkEnumerateInstanceVersion
@ stdcall wine_vkEnumeratePhysicalDeviceGroups(ptr ptr ptr)
@ stdcall wine_vkEnumeratePhysicalDevices(ptr ptr ptr)
@ stdcall wine_vkFlushMappedMemoryRanges(ptr long ptr)
@ stdcall wine_vkFreeCommandBuffers(ptr int64 long ptr)
@ stdcall wine_vkFreeDescriptorSets(ptr int64 long ptr)
@ stdcall wine_vkFreeMemory(ptr int64 ptr)
@ stdcall wine_vkGetBufferMemoryRequirements(ptr int64 ptr)
@ stdcall wine_vkGetBufferMemoryRequirements2(ptr ptr ptr)
@ stdcall wine_vkGetDescriptorSetLayoutSupport(ptr ptr ptr)
@ stub vkGetDeviceGroupPeerMemoryFeatures
@ stub vkGetDeviceGroupPresentCapabilitiesKHR
@ stub vkGetDeviceGroupSurfacePresentModesKHR
@ stdcall wine_vkGetDeviceMemoryCommitment(ptr int64 ptr)
@ stdcall wine_vkGetDeviceProcAddr(ptr str)
@ stdcall wine_vkGetDeviceQueue(ptr long long ptr)
@ stub vkGetDeviceQueue2
@ stub vkGetDisplayModePropertiesKHR
@ stub vkGetDisplayPlaneCapabilitiesKHR
@ stub vkGetDisplayPlaneSupportedDisplaysKHR
@ stdcall wine_vkGetEventStatus(ptr int64)
@ stdcall wine_vkGetFenceStatus(ptr int64)
@ stdcall wine_vkGetImageMemoryRequirements(ptr int64 ptr)
@ stdcall wine_vkGetImageMemoryRequirements2(ptr ptr ptr)
@ stdcall wine_vkGetImageSparseMemoryRequirements(ptr int64 ptr ptr)
@ stdcall wine_vkGetImageSparseMemoryRequirements2(ptr ptr ptr ptr)
@ stdcall wine_vkGetImageSubresourceLayout(ptr int64 ptr ptr)
@ stdcall wine_vkGetInstanceProcAddr(ptr str)
@ stub vkGetPhysicalDeviceDisplayPlanePropertiesKHR
@ stub vkGetPhysicalDeviceDisplayPropertiesKHR
@ stub vkGetPhysicalDeviceExternalBufferProperties
@ stub vkGetPhysicalDeviceExternalFenceProperties
@ stub vkGetPhysicalDeviceExternalSemaphoreProperties
@ stdcall wine_vkGetPhysicalDeviceFeatures(ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceFeatures2(ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceFormatProperties(ptr long ptr)
@ stdcall wine_vkGetPhysicalDeviceFormatProperties2(ptr long ptr)
@ stdcall wine_vkGetPhysicalDeviceImageFormatProperties(ptr long long long long long ptr)
@ stdcall wine_vkGetPhysicalDeviceImageFormatProperties2(ptr ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceMemoryProperties(ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceMemoryProperties2(ptr ptr)
@ stub vkGetPhysicalDevicePresentRectanglesKHR
@ stdcall wine_vkGetPhysicalDeviceProperties(ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceProperties2(ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceQueueFamilyProperties(ptr ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceQueueFamilyProperties2(ptr ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceSparseImageFormatProperties(ptr long long long long long ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceSparseImageFormatProperties2(ptr ptr ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceSurfaceCapabilitiesKHR(ptr int64 ptr)
@ stdcall wine_vkGetPhysicalDeviceSurfaceFormatsKHR(ptr int64 ptr ptr)
@ stdcall wine_vkGetPhysicalDeviceSurfacePresentModesKHR(ptr int64 ptr long)
@ stdcall wine_vkGetPhysicalDeviceSurfaceSupportKHR(ptr long int64 ptr)
@ stdcall wine_vkGetPhysicalDeviceWin32PresentationSupportKHR(ptr long)
@ stdcall wine_vkGetPipelineCacheData(ptr int64 ptr ptr)
@ stdcall wine_vkGetQueryPoolResults(ptr int64 long long long ptr int64 long)
@ stdcall wine_vkGetRenderAreaGranularity(ptr int64 ptr)
@ stdcall wine_vkGetSwapchainImagesKHR(ptr int64 ptr ptr)
@ stdcall wine_vkInvalidateMappedMemoryRanges(ptr long ptr)
@ stdcall wine_vkMapMemory(ptr int64 int64 int64 long ptr)
@ stdcall wine_vkMergePipelineCaches(ptr int64 long ptr)
@ stdcall wine_vkQueueBindSparse(ptr long ptr int64)
@ stdcall wine_vkQueuePresentKHR(ptr ptr)
@ stdcall wine_vkQueueSubmit(ptr long ptr int64)
@ stdcall wine_vkQueueWaitIdle(ptr)
@ stdcall wine_vkResetCommandBuffer(ptr long)
@ stdcall wine_vkResetCommandPool(ptr int64 long)
@ stdcall wine_vkResetDescriptorPool(ptr int64 long)
@ stdcall wine_vkResetEvent(ptr int64)
@ stdcall wine_vkResetFences(ptr long ptr)
@ stdcall wine_vkSetEvent(ptr int64)
@ stdcall wine_vkTrimCommandPool(ptr int64 long)
@ stdcall wine_vkUnmapMemory(ptr int64)
@ stdcall wine_vkUpdateDescriptorSetWithTemplate(ptr int64 int64 ptr)
@ stdcall wine_vkUpdateDescriptorSets(ptr long ptr long ptr)
@ stdcall wine_vkWaitForFences(ptr long ptr long int64)
