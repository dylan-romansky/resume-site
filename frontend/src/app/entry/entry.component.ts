import { Component, OnInit } from '@angular/core';
import { Validators, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.css']
})
export class EntryComponent {
	form: any;

	constructor(private fb: FormBuilder) {}

	ngOnInit(): void {
		this.form = this.fb.group({
			name: ["", Validators.required],
			type: ["", Validators.required],
			title: [""],
			startdate: ["", Validators.required],
			enddate: [""],
			content: ["", Validators.required]
		});
		this.form.valueChanges.subscribe(console.log);
	}

	onSubmit() {
		console.log(this.form);
	}
}
