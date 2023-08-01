builtin.module attributes {gpu.container_module} {
  "gpu.module"() ({
    "gpu.func"() ({
    ^0(%arg : memref<4x4xindex>):
      %0 = "arith.constant"() {"value" = 2 : index} : () -> index
      %1 = "gpu.global_id"() {"dimension" = #gpu<dim x>} : () -> index
      %2 = "gpu.global_id"() {"dimension" = #gpu<dim y>} : () -> index
      %3 = "arith.constant"() {"value" = 4 : index} : () -> index
      %4 = "arith.muli"(%1, %3) : (index, index) -> index
      %5 = "arith.addi"(%4, %2) : (index, index) -> index

      "memref.store"(%5, %arg, %1, %2) {"nontemporal" = false} : (index, memref<4x4xindex>, index, index) -> ()
      "gpu.return"() : () -> ()
    }) {"function_type" = (memref<4x4xindex>) -> (),
        "gpu.kernel",
        "sym_name" = "fill"
       } : () -> ()
    "gpu.module_end"() : () -> ()
  }) {"sym_name" = "gpu"} : () -> ()
}