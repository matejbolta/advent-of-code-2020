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
  content |> one_three_difference
(*  *)


(* Slovarji za memoizacijo *)
type 'a tree = Empty | Node of 'a tree * 'a * 'a tree (* trees will be used as dictionaries *)
(*  *)
let leaf x = Node (Empty, x, Empty)
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
  | None -> failwith "option type je none"
(*  *)
let dict_memo = ref Empty
  (* MEMOIZACIJA - za shranjevanje memoiziranih counterjev možnosti *)
  (* je referenca, ker jo aktivno spreminjamo in je globalna spremenljivka *)
(*  *)
let rec number_of_options last_element dict_opt input =
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
(*  *)


let naloga2 content = (* MEMOIZACIJA *)
  let l = content in
  let input = (0 :: l) @ [(List.hd (List.rev l)) + 3] in (* doda 0 na začetek in max+3 na konec seznama *)
  let dict_opt = build_dictionary input in (* slovar možnosti za n-je, 'naslednike' od m *)

  number_of_options 0 !dict_opt input (* prvo število je vedno 0, dict_opt je vendno enak *)
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

  let start1 = Sys.time () in
  let s1 = naloga1 content |> string_of_int in
  let end1 = Sys.time () in

  let start2 = Sys.time ()  in
  let s2 = naloga2 content |> string_of_int in
  let end2 = Sys.time () in

  let time1 = string_of_int (int_of_float (1000. *. (end1 -. start1))) ^ " ms" in
  let time2 = string_of_int (int_of_float (1000. *. (end2 -. start2))) ^ "ms" in
  
  write_file ("2020/out/day_" ^ day ^ "_1.out") s1;
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s1 ^ " in " ^ time1);
  write_file ("2020/out/day_" ^ day ^ "_2.out") s2;
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s2 ^ " in " ^ time2)
(*  *)

(*
Dan 11:
Prva naloga je bila vaja iz uporabe zank in referenc, kar se mi zdi kar lepo.
Druga naloga je bila kombinacija referenc in uporabe -memoizacije- v ocamlu.
Mučna izkušnja. Morda je malo proceduralno, ampak vseeno kar lepo.
Implementiral sem tudi slovarje kot search treeje kar je kr najs :)
*)