let day = "8"

(* https://stackoverflow.com/questions/37091784/ *)
let replace l pos a  = List.mapi (fun i x -> if i = pos then a else x) l
let make_triplet row = (* ukaz, num, bool *)
  (String.sub row 0 3,
  String.sub row 4 (String.length row - 4),
  false)
(*  *)
let izvedi_ukaze list' = (*triplet list, vrne (bool, acc) *)
  let len = List.length list' in
  let get_num num =
    let abs = int_of_string (String.sub num 1 (String.length num - 1)) in
    if String.get num 0 = '+' then abs
    else (* String.get num 0 = '-' *) (-abs)
  in
  let get_new_r_i_acc r_i acc ukaz num =
    match ukaz with
    | "nop" -> (r_i + 1, acc)
    | "jmp" -> (max 0 (r_i + get_num num), acc)
    | "acc" -> (r_i + 1, acc + get_num num)
    | _ -> failwith "napaka : izvedi_ukaze : get_new_r_i_acc"
  in
  let rec izvedi_aux r_i acc list =
    if r_i >= len then (true, acc) (* Smo na koncu ukazov *)
    else
      let (ukaz, num, state) = List.nth list r_i in
      if state then (false, acc) (* Nismo na koncu, se zaloopamo *)
      else
        let new_r_i, new_acc = get_new_r_i_acc r_i acc ukaz num in
        let new_list = replace list r_i (ukaz, num, true) in
        izvedi_aux new_r_i new_acc new_list
  in
  izvedi_aux 0 0 list'
(*  *)


let naloga1 content =
  let s = content
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map make_triplet
    |> izvedi_ukaze
    |> snd
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s);
  s
(*  *)


let rec acc_from_corrected_list last_changed_i og_list =
  let list_slice list i =
    let rec aux acc cur_i = function
      | [] -> List.rev acc
      | x :: xs ->
        if cur_i >= i then aux (x :: acc) (cur_i + 1) xs
        else aux acc (cur_i + 1) xs
    in
    aux [] 0 list
  in
  let first_that_needs_changing list = (* list -> index *)
    let rec aux i list' =
      let _ = try List.nth list' 0 with _ -> failwith "druga" in
      match List.nth list' 0 with
      | ("nop", _, _) | ("jmp", _, _) -> i
      | _ -> aux (i + 1) (List.tl list')
    in
    aux 0 list
  in
  let get_new_i og_list old_i =
    let sez = list_slice og_list (old_i + 1) in
    let sez_i = first_that_needs_changing sez in
    old_i + 1 + sez_i
  in
  let get_new_list og_list i =
    let _ = try List.nth og_list i with _ -> failwith "tretja" in
    match List.nth og_list i with
    | ("jmp", num, bool) -> replace og_list i ("nop", num, bool)
    | ("nop", num', bool') -> replace og_list i ("jmp", num', bool')
    | _ -> failwith "napaka  get_new_list"
  in
  let change_i_og_list og_list old_i =
    let new_i = get_new_i og_list old_i in
    let new_list = get_new_list og_list new_i in
    (new_list, new_i)
  in
  (* Zgoraj lokalne definicije, spodaj potek *)
  let (cur_list, changed_i) = change_i_og_list og_list last_changed_i in
  let result = izvedi_ukaze cur_list in
  if fst result (* = true *) then snd result (* smo prišli do konca seznama ukazov, vrnemo rešitev (akumulator) *)
  else acc_from_corrected_list changed_i og_list (* na cur_list smo se nekje zaloopali, poskusimo naslednji indeks *)
(*  *)


let naloga2 content =
  let s = content
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map make_triplet (* og_list *)
    |> acc_from_corrected_list (-1)
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s);
  s
(*  *)


let _ =
  let preberi_datoteko ime_datoteke =
    let chan = open_in ime_datoteke in
    let vsebina = really_input_string chan (in_channel_length chan) in
    close_in chan;
    vsebina
  in
  let izpisi_datoteko ime_datoteke vsebina =
    let chan = open_out ime_datoteke in
    output_string chan vsebina;
    close_out chan
  in

  let vsebina_datoteke = preberi_datoteko ("2020/data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke in
  let odgovor2 = naloga2 vsebina_datoteke in

  izpisi_datoteko ("2020/out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("2020/out/day_" ^ day ^ "_2.out") odgovor2
(*  *)

(*
Day 8: Zelo lepa rešitev, tako prve kot druge naloge. Funkcijska, z lepo strukturo podaktov.
*)