let day = "11"


let count_occupied m n tabela =
  let counter = ref 0 in
  let rows = Array.length tabela in
  let cols = Array.length (tabela.(0)) in
  let startm = max 0 (m - 1) in
  let endm = min (rows -  1) (m + 1) in
  let startn = max 0 (n - 1) in
  let endn = min (cols -  1) (n + 1) in
  for i = startm to endm do
    for j = startn to endn do
      if ((i, j) <> (m, n)) && (tabela.(i).(j) = "#") then
        counter := !counter + 1
    done;
  done;
  !counter
(*  *)
let change_value tabela m n =
  if tabela.(m).(n) = "L" then
    let _ = tabela.(m).(n) <- "#" in
    tabela_ref := tabela
  else if tabela.(m).(n) = "#" then
    let _ = tabela.(m).(n) <- "L" in
    tabela_ref := tabela
  else failwith "ni ne L ne #"
(*  *)
let make_step () =
  let stara_tabela_ref = ref (Array.copy !tabela_ref) in
  for m = 0 to Array.length !stara_tabela_ref - 1 do
    for n = 0 to Array.length (!stara_tabela_ref).(0) - 1 do
      let occupied = count_occupied m n !stara_tabela_ref in
      if (!stara_tabela_ref).(m).(n) = "L" && occupied = 0 then
        change_value (!stara_tabela_ref) m n
      else if (!stara_tabela_ref).(m).(n) = "#" && occupied >= 4 then
        change_value (!stara_tabela_ref) m n
    done;
  done;
  ()
(*  *)
let rec play_steps () =
  let stara_tabela = Array.copy !tabela_ref in
  let _ = make_step () in
  if stara_tabela = !tabela_ref then ()
  else play_steps ()
(*  *)
let count_all_occupied tabela =
  let counter = ref 0 in
  for m = 0 to Array.length tabela - 1 do
    for n = 0 to Array.length (tabela.(0)) - 1 do
      if tabela.(m).(n) = "#" then
        counter := !counter + 1
    done;
  done;
  !counter
(*  *)


let naloga1 content =
  let tabela_ref = ref (Array.of_list content) in

  play_steps ();

  count_all_occupied !tabela_ref
(*  *)


let naloga2 content = "unsolved"
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
    |> List.map (Str.split (Str.regexp ""))
    |> List.map Array.of_list
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
prva naloga bi morala delati, pa ne dela. Nekaj je narobe z
načinom ocamlovega shranjevanja spremenljivk / referenc.
(Delujoča) rešitev (obe nalogi) napisana v pythonu.
*)