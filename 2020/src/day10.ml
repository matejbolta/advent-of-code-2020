let day = "10"


let one_three_difference input =
  let one_counter, three_counter = ref 0, ref 0 in
  for i = 0 to List.length input - 1 do 
    if i = 0 && (List.nth input 0) = 1 then
      incr one_counter
    else if i = 0 && (List.nth input 0) = 3 then
      incr three_counter
    else
      let delta = List.nth input i - List.nth input (i - 1) in
      if delta = 1 then
        incr one_counter
      else if delta = 3 then
        incr three_counter
  done;
  !one_counter * (!three_counter + 1) (* +1 last adapter to device *)
(*  *)


let naloga1 content = (* 1904 on my input *)
  content |> one_three_difference |> string_of_int
(*  *)


type 'a tree = Empty | Node of 'a tree * 'a * 'a tree (* trees will be used as dictionaries *)
(*  *)
let leaf x = Node (Empty, x, Empty)
(*  *)
let rec print_dict dict = match dict with
  | Empty -> ()
  | Node (l, (k, v), d) ->
    print_dict l; (* ; vzame 2 unit expresiona in izvede oba, vrne unit *)
    print_string (string_of_int k ^ " : ");
    print_endline(String.concat " " (List.map string_of_int v));
    (* print_string (k ^ " : "); print_int v; print_newline (); *)
    print_dict d
(*  *)
let rec dict_get key dict =
  match dict with
  | Node (_, (k, v), _) when k = key -> Some v
  | Node (l, (k, _), _) when k > key -> dict_get key l
  (* | Node (_, _, d) -> dict_get key d *)
  | Node (_, (k, _), d) when k < key -> dict_get key d
  | _ -> None
(*  *)
let rec dict_insert key value dict =
  match dict with
  | Empty -> leaf (key, value)
  | Node (l, (k, v), d) ->
    if k = key then Node (l, (key, value), d)
    else if key < k then Node (dict_insert key value l, (k, v), d)
    else Node (l, (k, v), dict_insert key value d)
(*  *)
let build_dictionary input = (* Very procedural *) (* int list -> (int * int list) tree ref *)
  let dicty = ref Empty in
  let len = List.length input in
  let nth i = List.nth input i in
  for i = 0 to len - 1 do
    let x = nth i in
    if i < len - 3 then (
      if nth (i+3) - x <= 3 then
        dicty := (dict_insert x [nth (i+1); nth (i+2); nth (i+3)] !dicty)
      else if nth (i+2) - x <= 3 then
        dicty := (dict_insert x [nth (i+1); nth (i+2)] !dicty)
      else
        dicty := (dict_insert x [nth (i+1)] !dicty)
    )
    else if i < len - 2 then (
      if nth (i+2) - x <= 3 then
        dicty := (dict_insert x [nth (i+1); nth (i+2)] !dicty)
      else
        dicty := (dict_insert x [nth (i+1)] !dicty)
    )
    else if i < len - 1 then (
      dicty := (dict_insert x [nth (i+1)] !dicty)
    )
    else
      dicty := (dict_insert x [] !dicty)
  done;
  dicty
(*  *)
let option_type_to_x dict_opt last_element = function
  | Some x -> x
  | None ->
    print_dict dict_opt;
    print_endline (string_of_int last_element ^ " to je tale ključ");
    failwith "option type je none"
(*  *)
let rec number_of_options last_element dict_opt input =
  let dict_memo = ref Empty in (* za shranjevanje memoiziranih števil možnosti od m *)
  let rec aux () =
      let get_memo (x: int) dict_opt =
        let resit = dict_get x !dict_memo in
        match resit with
        | Some r -> r
        | None ->
          let r = number_of_options x dict_opt input in
          let _ = (dict_memo := (dict_insert x r !dict_memo)) in
          r
      in
    let possible : (int list) = option_type_to_x dict_opt last_element (dict_get last_element dict_opt) in
    let nth i = List.nth possible i in
    let len = List.length possible in
    if len = 3 then
      get_memo (nth 0) dict_opt + get_memo (nth 1) dict_opt + get_memo (nth 2) dict_opt
    else if len = 2 then
      get_memo (nth 0) dict_opt + get_memo (nth 1) dict_opt
    else if len = 1 then
      get_memo (nth 0) dict_opt
    else 1 (* possible = [] *)
  in
  aux ()
(*  *)




let input = [0;1;2;5;6;9;10;11;12;13;16;19;20;21;22;23;26;27;28;29;30;33;34;35;36;37;40;41;42;43;46;47;48;51;54;55;58;59;62;63;64;65;68;69;70;73;76;77;78;81;82;83;84;87;90;91;92;93;94;97;98;99;100;103;106;107;108;109;112;113;114;115;116;119;120;121;122;123;126;127;128;129;132;133;134;135;138;139;140;141;142;145;146;147;148;149;152]
(*  *)
let dict_opt = (build_dictionary input) (* slovar možnosti za n-je, naslednike od m *)


(* let r = number_of_options 0 !dict_opt input *)
(* 02:02 start *)




let naloga2 content = "unsolved"
  (* let l = content in *)
  (* let input = (0 :: l) @ [(List.hd (List.rev l)) + 3] in *)

(*  *)


let _ =
  let read_file file_name =
    let chan = open_in file_name in
    let content = really_input_string chan (in_channel_length chan) in
    close_in chan;
    content
  in
  let write_file file_name content =
    let chan = open_out file_name in
    output_string chan content;
    close_out chan
  in

  let content = read_file ("2020/data/day_" ^ day ^ ".in")
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map int_of_string
    |> List.sort compare
  in

  let s1 = naloga1 content in
  let s2 = naloga2 content in
  
  write_file ("2020/out/day_" ^ day ^ "_1.out") s1;
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s1);
  write_file ("2020/out/day_" ^ day ^ "_2.out") s2;
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s2)
(*  *)